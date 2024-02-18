import pandas as pd

df= pd.read_excel('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\Random Data\\FinancialsSampleData\\Financials Sample Data.xlsx',sheet_name='Financials')
df=df.dropna()
df=df.drop_duplicates()
df=df.drop(columns=['Currency','Scenario'])

for index in df.index:
    if df.loc[index,'Year']<2019:
        df.loc[index,'Year'] = 'Old Version'
    else:
        pass
df['Jan'] = df['Jan']/1000000
df['Feb'] = df['Feb']/1000000
df['Mar'] = df['Mar']/1000000
df['Apr'] = df['Apr']/1000000
df['May'] = df['May']/1000000
df['Jun'] = df['Jun']/1000000
df['Jul'] = df['Jul']/1000000
df['Aug'] = df['Aug']/1000000
df['Sep'] = df['Sep']/1000000


df=df.rename(columns={'Jan':'Jan (in million)'})
print(df.to_string())
print(df.describe().to_string())
