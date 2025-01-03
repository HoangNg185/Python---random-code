list1 = ['apple', 'pixa', 'nut', 'booba']
list2 = [1, 2, 3, 5, 4, 2]

f = open('testing note pad writing.txt', 'a+')


def prewrite(*args):
    for i in args:
        print(f'<ul>{i}</ul>')


prewrite(*list1)

import pandas as pd

df = pd.read_excel('C:\\Users\\Liam\\OneDrive - Seneca\\Desktop\\1. Me\\My hln excel.xlsx', sheet_name='Sheet1')
print(df.to_string())
for i in df.index:
    list3 = df.loc[i, 'data']
    list4 = df.loc[i, 'item']
    print(f'<{list3}>{list4}</{list3}>')
    f.write(f'<{list3}>{list4}</{list3}>\n')

f.close()
