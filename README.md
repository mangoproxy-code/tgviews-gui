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
