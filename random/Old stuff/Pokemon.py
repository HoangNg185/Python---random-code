import warnings

import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

warnings.filterwarnings("ignore")

df = pd.read_csv('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\Leaning SQL\\kaggle\\facebook_reviews.csv')
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', False)

df = df.drop(columns=['at'])
print(df.columns)
print(df['reviewId'].is_unique)
