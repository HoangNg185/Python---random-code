import pandas as pd
df=pd.read_excel('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\HTML projects\\5. April - key,value\\key, value.xlsx', sheet_name='Jean style')

#directory = input('Your directory (dont forget \\\): ')
#sheet_name =input('Name of the table: ')
#df=pd.read_excel(directory,sheet_name=sheet_name)

for i in df.index:
    col1=df.loc[i, 'ID']
    col2=df.loc[i,'Style']
    print(f'<tr>\n    <td>{col1}</td>\n    <td>{col2}</td>\n</tr>')

column_name=df.columns.tolist()
kwargs = {name: [] for name in column_name}
print(kwargs)


