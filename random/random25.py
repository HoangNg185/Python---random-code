import pandas as pd

df =pd.read_excel('Data manipulation.xlsx')

prime=[]
for i in range(min(df['No']),max(df['No'])+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        prime.append(i)

for right_cell in range(0, max(df['No'])):
    df.loc[right_cell, 'Prime no']= 'asd'

print(df.to_string())
print(prime)

