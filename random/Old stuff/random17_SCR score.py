from bs4 import BeautifulSoup
from selenium import webdriver

# some time if website use JS, we can't use bs4 as usual
# URL of the webpage to scrape
url = "https://www.canada.ca/en/immigration-refugees-citizenship/corporate/mandate/policies-operational-instructions-agreements/ministerial-instructions/express-entry-rounds.html"

# Start a WebDriver session
driver = webdriver.Chrome()  # You need to have Chrome WebDriver installed and in your PATH

# Load the webpage
driver.get(url)

# Wait for the JavaScript to load the table data
# You may need to adjust the sleep time based on the page loading speed
import time

time.sleep(10)

# Parse the HTML content after the JavaScript has loaded the table data
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all <td> elements
td_elements = soup.find_all('td')

# Extract and print the text content of each <td> element
print('#, Date, Type, invitations issued, Lowest candidate')
for td in td_elements:
    print(td.get_text())

# Close the WebDriver session
driver.quit()
