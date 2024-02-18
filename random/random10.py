import pandas as pd
import numpy as np
from pylab  import rcParams
import matplotlib.pyplot as plt
df1 = pd.read_excel('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\KCC Customer and Orders DB.xlsx', sheet_name='Flat File')

df1= df1.drop_duplicates()
df1= df1.dropna(how='any')
df1['OrderDate']=pd.to_datetime(df1['OrderDate'])

print('Revenue Per Cookie analysist\n',df1['RevenuePerCookie'].describe().to_string())


rcParams['figure.figsize']=10,5
df1.boxplot(column='CookieID')
plt.grid(True, axis='y')
plt.ylabel('CookieID')
plt.xticks([1], ['RevenuePerCookie'])

plt.show()