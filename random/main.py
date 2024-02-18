import pandas as pd

df=pd.read_excel('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\Job Applied part 2.xlsx')
result_dict = df.set_index('Title')['Company name'].to_dict()

df['notes'] = df['notes'].fillna(' ')


print(df.to_string())

for key,values in result_dict.items():
    print(f'{values}---------------{key}')
