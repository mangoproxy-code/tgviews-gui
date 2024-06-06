import aiohttp
import asyncio
from re import search, compile
from aiohttp_socks import ProxyConnector
from tkinter import Tk, Label, Entry, Button, StringVar, IntVar, Text, END
from tkinter.ttk import Progressbar
from threading import Thread
import webbrowser

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
REGEX = compile(
    r"(?:^|\D)?(("
    + r"(?:[1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"\."
    + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"\."
    + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"\."
    + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"):" 
    + r"(?:\d|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}"
    + r"|65[0-4]\d{2}|655[0-2]\d|6553[0-5])"
    + r")(?:\D|$)"
)

class Telegram:
    def __init__(self, channel: str, post: int, tasks: int, update_log, update_progress) -> None:
        self.tasks = tasks
        self.channel = channel
        self.post = post
        self.update_log = update_log
        self.update_progress = update_progress
        self.cookie_error = 0
        self.sucsess_sent = 0
        self.failled_sent = 0
        self.token_error = 0
        self.proxy_error = 0

    async def request(self, proxy: str, proxy_type: str):
        connector = ProxyConnector.from_url(f'socks5://{proxy}')
        jar = aiohttp.CookieJar(unsafe=True)
        async with aiohttp.ClientSession(cookie_jar=jar, connector=connector) as session:
            try:
                async with session.get(
                    f'https://t.me/{self.channel}/{self.post}?embed=1&mode=tme', 
                    headers={
                        'referer': f'https://t.me/{self.channel}/{self.post}',
                        'user-agent': user_agent
                    }, timeout=aiohttp.ClientTimeout(total=5)
                ) as embed_response:
                    if jar.filter_cookies(embed_response.url).get('stel_ssid'):
                        views_token = search('data-view="([^"]+)"', await embed_response.text())
                        if views_token:
                            views_response = await session.post(
                                'https://t.me/v/?views=' + views_token.group(1), 
                                headers={
                                    'referer': f'https://t.me/{self.channel}/{self.post}?embed=1&mode=tme',
                                    'user-agent': user_agent, 'x-requested-with': 'XMLHttpRequest'
                                }, timeout=aiohttp.ClientTimeout(total=5)
                            )
                            if (await views_response.text() == "true" and views_response.status == 200):
                                self.sucsess_sent += 1
                                self.update_progress()
                            else:
                                self.failled_sent += 1
                        else:
                            self.token_error += 1
                    else:
                        self.cookie_error += 1
            except:
                self.proxy_error += 1
            finally:
                jar.clear()

    async def run_rotated_task(self, proxy, proxy_type):
        while self.sucsess_sent < self.tasks:
            await asyncio.wait(
                [asyncio.create_task(self.request(proxy, proxy_type)) 
                for _ in range(self.tasks)]
            )
            self.update_log(self.sucsess_sent, self.failled_sent, self.proxy_error)

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Telegram Auto Views")
        self.root.resizable(False, False)

        self.channel_label = Label(root, text="Channel")
        self.channel_label.grid(row=0, column=0)
        self.channel_entry = Entry(root, textvariable=StringVar())
        self.channel_entry.grid(row=0, column=1)

        self.post_label = Label(root, text="Post Number")
        self.post_label.grid(row=1, column=0)
        self.post_entry = Entry(root, textvariable=IntVar())
        self.post_entry.grid(row=1, column=1)

        self.proxy_label = Label(root, text="Proxy (user:password@host:port)")
        self.proxy_label.grid(row=2, column=0)
        self.proxy_entry = Entry(root, textvariable=StringVar())
        self.proxy_entry.grid(row=2, column=1)

        self.mango_proxy_link = Label(root, text="MangoProxy", fg="blue", cursor="hand2")
        self.mango_proxy_link.grid(row=2, column=2)
        self.mango_proxy_link.bind("<Button-1>", lambda e: self.open_mango_proxy())

        self.views_label = Label(root, text="Number of Views")
        self.views_label.grid(row=3, column=0)
        self.views_entry = Entry(root, textvariable=IntVar())
        self.views_entry.grid(row=3, column=1)

        self.start_button = Button(root, text="Start", command=self.start)
        self.start_button.grid(row=4, column=1)

        self.progress_label = Label(root, text="Progress")
        self.progress_label.grid(row=5, column=0)
        self.progress = Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.grid(row=5, column=1)

        self.log_label = Label(root, text="Log")
        self.log_label.grid(row=6, column=0)
        self.log_text = Text(root, height=10, width=50)
        self.log_text.grid(row=7, column=0, columnspan=3)

    def open_mango_proxy(self):
        webbrowser.open_new("https://dashboard.mangoproxy.com/signup?ref=soft")

    def update_progress(self):
        self.progress['value'] += 1

    def update_log(self, success, failed, proxy_error):
        self.log_text.delete(1.0, END)
        self.log_text.insert(END, f"Sent: {success}\n")
        self.log_text.insert(END, f"Failed: {failed}\n")
        self.log_text.insert(END, f"Proxy Error: {proxy_error}\n")

    def start(self):
        channel = self.channel_entry.get()
        post = int(self.post_entry.get())
        proxy = self.proxy_entry.get()
        views = int(self.views_entry.get())

        self.progress['maximum'] = views
        self.progress['value'] = 0

        api = Telegram(channel, post, views, self.update_log, self.update_progress)
        Thread(target=lambda: asyncio.run(api.run_rotated_task(proxy, "socks5"))).start()

if __name__ == "__main__":
    root = Tk()
    gui = GUI(root)
    root.mainloop()
