import pandas as pd
from myMath import Finance

df = pd.read_excel('Data manipulation.xlsx')
df['No2']=int()
df['collatz_return_n']=int()
df['Prime number']=int()

def collatz_return_n(num: int) -> int:
    n = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        n += 1
    return n

question2 = Finance()
for i in df.index:
    df.loc[i,'No2']=int(df.loc[i,'No'])*3+1
    df.loc[i,'collatz_return_n']=collatz_return_n(df.loc[i,'No'])
    df.loc[i,'Prime number']=question2.isprime(df.loc[i,'No'])

print(df.to_string())
print(df['Prime number'].describe())

#df.to_excel('Data manipulation2.xlsx',index=False)
