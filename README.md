# Telegram Auto Views GUI

This project is a Python-based GUI application that automates the process of increasing views on a Telegram post. It utilizes proxy configurations to repeatedly open the specified Telegram post, aiming to increase the view count.

## Features

- GUI for easy input of proxy configuration and Telegram post URL
- Supports SOCKS5 proxies
- Concurrent requests for faster view count increase
- Progress bar to show the progress
- Real-time log updates
- Stop and save functionality

## Prerequisites

- Python 3.x
- aiohttp
- aiohttp_socks
- tkinter

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/mangoproxy-code/tgviews-gui.git
    cd tgviews-gui
    ```

2. Install the required Python packages:
    ```sh
    pip install aiohttp aiohttp_socks
    ```

## Usage

1. Run the `telegram_auto_views_gui.py` script:
    ```sh
    python telegram_auto_views_gui.py
    ```

2. Use the GUI to:
    - Input your proxy configuration in the format `user:password@host:port`.
    - Input the Telegram post URL.
    - Click "Start" to begin the process.
    - Click "Stop and Save" to stop the process and save the results.
    - Check the log for real-time updates.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Alex Whynot
