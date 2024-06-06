# Telegram Auto Views Bot

This project is a Python-based GUI application to increase views on a Telegram post using proxies. The application allows users to input proxy credentials, the number of views, and the Telegram post link. It simulates views using the specified proxies.

## Features

- GUI for easy input of details
- Supports SOCKS5 proxies
- Progress bar to show the progress of views
- Log display for successful, failed views, and proxy errors
- Clickable link to MangoProxy for easy proxy acquisition

## Prerequisites

- Python 3.x
- aiohttp
- aiohttp_socks
- tkinter

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the `telegram_auto_views_gui.py` script:
    ```sh
    python telegram_auto_views_gui.py
    ```

2. Fill in the following fields in the GUI:
    - **Channel**: The Telegram channel username.
    - **Post Number**: The Telegram post number.
    - **Proxy**: Proxy credentials in the format `user:password@host:port`.
    - **Number of Views**: The number of views you want to generate.

3. Click the "Start" button to begin the process.

## Files

- `telegram_auto_views_gui.py`: The main script to run the GUI application.
- `requirements.txt`: List of required Python packages.
- `.gitignore`: Git ignore file to exclude unnecessary files from the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
