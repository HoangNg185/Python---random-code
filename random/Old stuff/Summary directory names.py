import warnings

import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

warnings.filterwarnings("ignore")
df = pd.read_csv('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\Leaning SQL\\kaggle\\Pokemon.csv')
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)

import os

for dirname, _, filenames in os.walk('C:\\Users\\Liam\\PycharmProjects\\random code\\random'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
