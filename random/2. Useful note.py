import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FuncFormatter

pd.set_option('display.max_rows', None)

import os

for a, b, c in os.walk('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\Leaning SQL\\kaggle'):
    for i in c:
        # print(os.path.join(a,i))
        pass

df = pd.read_csv(
    'C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\Leaning SQL\\kaggle\\India dataset\\1.1 - India_Historical_Population_Density_Data.csv')
features = [['year', 'popu1ation_growth_rate', 'Population_Density', 'growth_rate']]
# -------------------------------------------------------------------------------------------------------------------------

pd.options.display.float_format = '{:.4f}'.format
stats = df.groupby('year')['popu1ation_growth_rate'].min()
print(stats)

plt.figure(figsize=(20, 12))
sns.histplot(data=df, x='year', kde=True, weights='popu1ation_growth_rate', bins=len(df['year'].unique()))
plt.ylabel('Sum of Population')

# -------------------------------------------------------------------------------------------------------------------------
formatter = FuncFormatter(lambda x, pos: f'{int(x):,}')
plt.gca().yaxis.set_major_formatter(formatter)

plt.tight_layout()
plt.show()

'''pd.options.display.float_format = '{:.4f}'.format
stats = df.groupby('year')['popu1ation_growth_rate'].min()
plt.figure(figsize=(10, 6))
plt.plot(stats.index, stats.values, marker='o', linestyle='-', color='b')
plt.xlabel('Year')
plt.ylabel('Minimum Population Growth Rate')
plt.title('Minimum Population Growth Rate by Year')
formatter = FuncFormatter(lambda x, pos: f'{int(x):,}')
plt.gca().yaxis.set_major_formatter(formatter)
plt.grid(True)
plt.tight_layout()
plt.show()'''
