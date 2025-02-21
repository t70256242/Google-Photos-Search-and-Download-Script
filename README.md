# Google Photos Search and Download Script

This script automates the process of searching for a player's photos on Google, navigating to the image results, and downloading the images. It uses Selenium for browser automation and handles various exceptions to ensure robustness.

---

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Error Handling](#error-handling)
7. [Limitations](#limitations)
8. [License](#license)

---

## Features

- **Google Search Automation**: Automates searching for a player's photos on Google.
- **Image Download**: Downloads images from the search results.
- **Exception Handling**: Handles common exceptions like `NoSuchElementException`, `TimeoutException`, and more.
- **Headless Mode Support**: Can run in headless mode for faster execution.
- **Randomized Delays**: Adds random delays to mimic human behavior and avoid detection.

---

## Requirements

- Python 3.7 or higher
- Selenium
- PyAutoGUI
- ChromeDriver (matching your Chrome browser version)
- Google Chrome browser

---

## Installation

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/).

2. **Install Required Libraries**:
   ```bash
   pip install selenium pyautogui requests
   ```

3. **Download ChromeDriver**:
   - Download the version of ChromeDriver that matches your Chrome browser version from [here](https://sites.google.com/chromium.org/driver/).
   - Add the ChromeDriver executable to your system's PATH or place it in the same directory as the script.

---

## Usage

1. **Run the Script**:
   ```bash
   python google_photo_search.py
   ```

2. **Enter Player's Name**:
   - When prompted, enter the name of the player whose photos you want to search and download.

3. **View Downloaded Images**:
   - The downloaded images will be saved in the same directory as the script with filenames like `{player}_download_{count}.jpg`.

---

## Configuration

### Chrome Options
The script uses the following Chrome options for browser configuration:
- `--disable-blink-features=AutomationControlled`: Disables automation detection.
- `--start-maximized`: Starts the browser in maximized mode.
- `--window-size=1280,800`: Sets the browser window size.
- `--disable-gpu`: Disables GPU acceleration (useful for headless mode).

### Headers
The script uses custom headers to mimic a real browser request:
```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://www.google.com/",
}
```

### Random Delays
The script uses random delays to mimic human behavior:
```python
time_series = [6, 8, 9]  # Random delays in seconds
time.sleep(random.choice(time_series))
```

---

## Error Handling

The script handles the following exceptions:
- `NoSuchElementException`: Element not found.
- `TimeoutException`: Timeout while waiting for an element.
- `StaleElementReferenceException`: Element reference is stale.
- `ElementNotInteractableException`: Element is not interactable.
- `WebDriverException`: General WebDriver error.
- `requests.RequestException`: Error during image download.

If an error occurs, the script will retry the operation up to 3 times before quitting.

---

## Limitations

- **Anti-Bot Mechanisms**: Some websites may detect and block automated scripts.
- **Headless Mode**: Certain websites may not work properly in headless mode.
- **Image Source**: The script assumes the image source is either a URL or a base64-encoded string.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Support

For issues or questions, please open an issue on the [GitHub repository](https://github.com/your-repo/google-photo-search).

---

## Example Output

```
Starting google photo search headless
Search query entered and submitted.
Found the image search result.
✅ Downloaded image: player_download_0.jpg
✅ Downloaded image: player_download_1.jpg
...
```

---

Enjoy using the Google Photos Search and Download Script! 🚀