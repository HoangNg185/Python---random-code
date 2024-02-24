import pandas as pd

df =pd.read_excel('Data manipulation.xlsx')

df['Right cell'] = ' '


for i in df['Right cell'].index:
    df.loc[i,'Right cell']
print(df.to_string())

