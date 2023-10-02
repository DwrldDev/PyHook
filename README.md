# PyHook
![image](https://user-images.githubusercontent.com/116701630/198017571-2b5e803e-a037-4547-8796-50d45ec2a835.png) 
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![GitHub stars](https://img.shields.io/github/stars/DwrldDev/PyHook.svg)](https://github.com/DwrldDev/PyHook/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/DwrldDev/PyHook.svg)](https://github.com/DwrldDev/PyHook/issues)
[![GitHub forks](https://img.shields.io/github/forks/DwrldDev/PyHook.svg)](https://github.com/DwrldDev/PyHook/network)



Discord Webhook spammer that uses proxies

![pyhook](https://github.com/DwrldDev/PyHook/assets/116701630/dc03b36a-9691-47a5-90f5-3335fca7d846)
![pyprox](https://github.com/DwrldDev/PyHook/assets/116701630/1c641f73-fe08-4990-b7ab-c05175acd8a8)
![dc](https://github.com/DwrldDev/PyHook/assets/116701630/34162019-aa98-4c83-980f-633b9a77621c)

# Proxy Spammer



The Proxy Spammer is a Python script that allows you to send messages to a Discord webhook through a list of HTTP proxies. You can use this tool for testing and educational purposes. The script provides a menu-driven interface for easy use.



Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.x
Required Python libraries (requests, colored, selenium)
Google Chrome web browser
Chrome WebDriver (chromedriver) for Selenium (compatible with your Chrome version)
Usage
Follow these steps to use the Proxy Spammer script:

Clone the repository to your local machine:


git clone https://github.com/DwrldDev/PyHook/

Navigate to the project directory

# install 

```
pip install -r requirements.txt 
```

Run the script:
```
python pyhook.py
```
# Follow the on-screen menu to choose the desired functionality:


Scrape and Save HTTP Proxies (Option 1): Scrapes HTTP proxies from a website and saves them to a CSV file.

Send Messages through Proxies (Option 2): Sends messages to a Discord webhook using the saved proxies.

Exit (Option 3): Exits the program.

Scrape and Save HTTP Proxies
Choosing Option 1 will:

Open a headless Chrome web browser using Selenium.

Navigate to the "https://free-proxy-list.net/" website to scrape proxy data.

Extract HTTP proxy information (IP address and port) and save it to a CSV file named "proxies.csv."

Inform you that the HTTP proxies have been saved to the CSV file.

# Send Messages through Proxies
Choosing Option 2 will:

Prompt you to enter the Discord webhook URL where you want to send messages.

Prompt you to enter the message you want to spam to the webhook.

Prompt you to enter the filename of the CSV file containing the list of proxies (e.g., "proxies.csv").

Iterate through the list of proxies.

For each proxy, send the specified message to the Discord webhook using the proxy.

Display status messages indicating whether the message was sent successfully or if there were any errors.

Handle rate limiting (if applicable) by waiting for the specified retry duration.

Inform you once the messages have been successfully spammed to the webhook.

# Important Notes
The script assumes that the HTTP proxy list is saved in a CSV file with the format "IP:Port" in the first column.

Proxies that support HTTPS are skipped when saving the list of proxies. This ensures that only HTTP proxies are used for sending messages.

The script handles rate limiting by waiting for the specified duration (in milliseconds) if the Discord API returns a rate-limiting response.

To use Selenium for web scraping, ensure that you have the Chrome WebDriver (chromedriver) installed and compatible with your Chrome browser version.

# Credits
This script was created by DwrldDev.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Disclaimer
Use this script responsibly and only for educational or legitimate testing purposes. Abusing proxies or web scraping may violate the terms of service of websites and services you interact with. Ensure you have the necessary permissions and rights before using this script.
