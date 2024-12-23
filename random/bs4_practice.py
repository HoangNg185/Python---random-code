import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup

url='https://www.hubertiming.com/results/2017GPTR10K'
sauce=urlopen(url)
soup=BeautifulSoup(sauce,'lxml')
all_a=soup.find_all('a')
get_text=soup.get_text()
#for links in all_a:
#    print(links.get('href'))
get_tr=soup.find_all('tr')
'''for row in get_tr:
    row_td=row.find_all('td')
str_cell=str(row_td)
clean_text=BeautifulSoup(str_cell,'lxml').get_text()
print(clean_text)'''

import re
list_rows=[]
for row in get_tr:
    cells=row.find_all('td')
    str_cell=str(cells)
    clean_text=re.compile('<.*?>')
    clean_text_2=(re.sub(clean_text,'',str_cell))
    list_rows.append(clean_text_2)
print(clean_text_2)
pd.set_option('display.max_columns',None)
df=pd.DataFrame(list_rows)
df1=df[0].str.split(',',expand=True)
df1[0].str.strip('[')
print(df1)