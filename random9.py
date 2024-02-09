import pandas as pd

df = pd.read_excel('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\KCC Customer and Orders DB.xlsx', sheet_name='Flat File')
df['OrderDate']=pd.to_datetime(df['OrderDate'])
df.loc[0,'CookieID']=1000

for x in df.index:
    if df.loc[x,'Quantity']>160:
        df.loc[x,'Notes'] = 'lots of order'
        df.loc[x,'Quantity']= 160
    if df.loc[x,'CookieName']=='Fortune Cookie':
        df.loc[x,'CookieName']='ChinaaaaaaaCookie'

print(df.to_string())

output_file='modified_orders.xlsx'
df.to_excel(output_file,index=False)