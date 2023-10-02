import csv
import requests
from time import sleep
from colored import fg, attr
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# Function to read proxies from a CSV file
def read_proxies_from_csv(filename):
    proxies_list = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            proxies_list.append(row[0])  # Assuming the IP:Port is in the first column
    return proxies_list

# Function to send messages through proxies
def send_message_through_proxies(webhook_url, message, proxies_list):
    try:
        successfully_spammed = False

        for proxy in proxies_list:
            proxies = {"http": f"http://{proxy}"}
            print(f"Sending message through proxy: {proxy}")
            response = requests.post(
                webhook_url,
                json={"content": message},
                params={'wait': True},
                proxies=proxies
            )
            try:
                if response.status_code in (204, 200):
                    if not successfully_spammed:
                        print(f"{fg(2)}Successfully spammed webhook{attr(0)}")
                        successfully_spammed = True
                    print(f"{fg(2)}Message sent{attr(0)}")
                elif response.status_code == 429:
                    print(f"{fg(3)}Rate limited ({response.json()['retry_after']}ms){attr(0)}")
                    sleep(response.json()["retry_after"] / 1000)
                else:
                    if not successfully_spammed:
                        print(f"{fg(1)}Unsuccessfully spammed webhook{attr(0)}")
                        successfully_spammed = True
                    print(f"{fg(1)}Error: {response.status_code}{attr(0)}")

                sleep(0.01)
            except KeyboardInterrupt:
                break

        print("Enter anything to continue. . . ", end="")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while sending the request: {str(e)}")

# Function to scrape and save HTTP proxies
def scrape_and_save_proxies():
    # Initialize the Selenium WebDriver (assuming you have WebDriver installed)
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options) 

    # Navigate to the webpage containing the table
    driver.get('https://free-proxy-list.net/')  # Replace with the actual URL

    try:
        # Find all the rows in the table (skip the first row as it contains headers)
        rows = driver.find_elements('xpath', '//tbody/tr[position()>1]')

        # Create a CSV file and write headers
        with open('proxies.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Loop through each row and extract the data for HTTP proxies only
            for row in rows:
                # Extract data from each column in the row
                columns = row.find_elements('tag name', 'td')
                if len(columns) >= 8:
                    https_support = columns[6].text

                    # Check if the proxy supports HTTPS, and if not, skip it
                    if https_support.lower() != "no":
                        continue

                    ip_address = columns[0].text
                    port = columns[1].text

                    # Write the data to the CSV file in the desired format
                    csv_writer.writerow([f'{ip_address}:{port}'])

        print("HTTP proxies saved to 'proxies.csv'")

    except Exception as e:
        print("Error:", e)

    # Close the WebDriver
    driver.quit()

if __name__ == "__main__":
    while True:
        art = '''
            ██████╗ ██╗   ██╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
            ██╔══██╗╚██╗ ██╔╝██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
            ██████╔╝ ╚████╔╝ ███████║██║   ██║██║   ██║█████╔╝ 
            ██╔═══╝   ╚██╔╝  ██╔══██║██║   ██║██║   ██║██╔═██╗ 
            ██║        ██║   ██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
            ╚═╝        ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═
                by DwrldDev
            '''
        print(art)
        print("Menu:")
        print("1. Scrape and Save HTTP Proxies")
        print("2. Send Messages through Proxies")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            scrape_and_save_proxies()
        elif choice == "2":
            webhook_url = input("Enter the Discord webhook URL: ")
            message = input("Enter the message to spam: ")
            proxy_filename = input("Enter the filename of the CSV with proxies: ")

            proxies_list = read_proxies_from_csv(proxy_filename)
            send_message_through_proxies(webhook_url, message, proxies_list)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")






