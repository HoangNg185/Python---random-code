import time
from time import strftime

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

start_time = time.time()

chrome_options = Options()
chrome_options.add_argument("--headless")
service = Service("C:\\Users\\Liam\\.cache\\selenium\\chromedriver\\win64\\131\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

df = pd.read_csv('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\1. Me\\stock_mysql.csv', index_col='ID')
today = strftime('%h %d, %H:%M')
df[today] = ''
# df=df.drop(columns=['stock_name','date_added','category','capital_value_at_added_date','relationships_and_notes'])

for i in df.index:
    name = df.loc[i, 'search_symbol']
    url = f"https://www.google.com/search?q=stock+{name}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(url, headers=headers)
    time.sleep(2)
    soup = BeautifulSoup(response.text, "html.parser")

    percentage = soup.find('span', {'jsname': 'rfaVEf'})
    changes = soup.find('span', {'jsname': 'qRSVye'})
    if percentage:
        df.loc[i, today] = f'{changes.get_text()[0]}{percentage.get_text()[1:-1]}'
        print(df.loc[i, today])
    else:
        df.loc[i, today] = 0

print(df.to_string())
df.to_csv('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\1. Me\\stock_mysql.csv')
end_time = time.time()
elapsed_time = end_time - start_time
print(f'Total time taken:{elapsed_time:.2f} seconds')
