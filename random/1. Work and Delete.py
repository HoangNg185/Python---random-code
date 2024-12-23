import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_option = Options()
chrome_option.add_argument('--headless')
service = Service("C:\\Users\\Liam\\.cache\\selenium\\chromedriver\\win64\\131\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_option)

url = 'https://www.wsj.com/?mod=wsjheader_logo'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

fine_1 = soup.find('div', {'class': 'e1sf124z8 css-1lys499-HeadlineTextBlock'})
print(fine_1)
