import numpy
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\KCC Customer and Orders DB.xlsx',sheet_name=4)
df=df[:10]
print(df.to_string())

ordertotal=df['OrderTotal']
RevenuePerCookie=df['RevenuePerCookie']
CostPerCookie=df['CostPerCookie']
print(ordertotal)
plt.plot(RevenuePerCookie,CostPerCookie)
plt.show()