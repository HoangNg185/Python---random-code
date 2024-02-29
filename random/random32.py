import pandas as pd

df = pd.read_excel('Data manipulation.xlsx')
df['No2']=int()
df['collatz_return_n']=int()

def collatz_return_n(num: int) -> int:
    n = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        n += 1
    return n

for i in df.index:
    df.loc[i,'No2']=int(df.loc[i,'No'])*3+1
    df.loc[i,'collatz_return_n']=collatz_return_n(df.loc[i,'No'])


print(df.to_string())