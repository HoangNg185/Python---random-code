import pandas as pd

df = pd.read_csv('WSJ.csv')
for i in df.index:
    title = df.loc[i, 'title']
    link = df.loc[i, 'link']
    print(f'<li><a href="{link}" target="_blank">{title}</a></li>')
