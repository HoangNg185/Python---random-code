import pandas as pd

df = pd.read_excel('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\1. Me\\1. My hln excel.xlsx', sheet_name='Word')

list = []
for i in df.index:
    list.append(df.loc[i, 'Word'])
print(list)
