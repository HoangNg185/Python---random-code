import pandas as pd

df=pd.read_excel('Data manipulation.xlsx',sheet_name='Company Note')
df['Notes']=str()
for index in df.index:
    print(type(df.loc[index,'% Gross Sale']))
    df.loc[index, 'Notes']=df.loc[index,'% Gross Sale']*100
df.to_excel('Data manipulation.xlsx',index=False)