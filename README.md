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

2. Fill in the following fields in the GUI:
    - **Channel**: The Telegram channel username.
    - **Post Numbers**: The Telegram post numbers. You can specify ranges (e.g., `1-10`) or individual posts (e.g., `4,5,6-10`).
    - **Proxy**: Proxy credentials in the format `user:password@host:port`.
    - **Number of Views per Post**: The number of views you want to generate for each post.

3. Click the "Start" button to begin the process.

## Files

- `telegram_auto_views_gui.py`: The main script to run the GUI application.
- `requirements.txt`: List of required Python packages.
- `.gitignore`: Git ignore file to exclude unnecessary files from the repository.

## Changelog

### v1.2.0
- **Improved Post Number Input**: Support for ranges and individual post numbers (e.g., `1-10`, `4,5,6-10`).
- **Number of Views per Post**: Each post now receives the specified number of views individually.
- **Detailed Logging**: Enhanced logging for better debugging and tracking of request attempts.
- **Increased Timeout and Retry Mechanism**: Improved request handling with increased timeout and retry mechanism to reduce proxy errors.
- **Added Delays**: Introduced delays between requests to avoid overwhelming the proxy service and reduce proxy errors.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support my project
Any donations can lead to improvements and updates
BTC donations:  ```
    1BFt6AiGK22sC6QP7s7sYzfFyaEz5PPw1j
    ```

## Author

Alex Whynot
