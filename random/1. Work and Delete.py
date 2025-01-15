import time
from datetime import datetime

import pandas as pd

df = pd.read_csv('timetable.csv')
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M').apply(
    lambda x: datetime.combine(datetime.today().date(), x.time()))
df['Due'] = 0
df['Due'] = df['Due'].astype(bool)


def run_time():
    while True:
        current_time = time.strftime('%H:%M:%S')
        print(current_time)
        time.sleep(1)


def run_table():
    while True:
        current_time = datetime.strptime(time.strftime('%c'), '%c')
        print(current_time)
        for i in df.index:
            if current_time > df.loc[i, 'Time']:
                df.loc[i, 'Due'] = True
            else:
                df.loc[i, 'Due'] = False
        print(df.to_string())
        print('-----------------------------------------------------')
        time.sleep(60)


run_table()
