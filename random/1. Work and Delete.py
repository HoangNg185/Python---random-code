import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)

df = pd.read_csv('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\bond_yields_benchmark.csv')
columns = ['date', 'no', '2yr', '3yr', '5yr', '7yr', '10yr', 'long', 'RRB']
df.fillna(0, inplace=True)
# convert 'date' to datetime then to year(interger)
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].dt.year
print(df.to_string())

# print(df.to_string())
year_of_RRB = []
for i in df.index:
    if df.loc[i, 'RRB'] > df.loc[i, '2yr']:
        year_of_RRB.append(df.loc[i, 'date'])
print(sorted(set(year_of_RRB)))
plt.plot(df['no'], df['2yr'], label='2yr')
plt.plot(df['no'], df['3yr'], label='3yr')
plt.plot(df['no'], df['5yr'], label='5yr')
plt.plot(df['no'], df['7yr'], label='7yr')
plt.plot(df['no'], df['10yr'], label='10yr')
plt.plot(df['no'], df['long'], label='long')
plt.plot(df['no'], df['RRB'], label='RRB')

plt.legend()
plt.show()
