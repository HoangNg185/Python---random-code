import time
from datetime import datetime

import pandas as pd
import pygame

df = pd.read_csv('timetable.csv')
df.columns = df.columns.str.strip()


def format_time(time_value):
    try:
        time_obj = datetime.strptime(time_value, '%I:%M %p')
        return time_obj.strftime('%H:%M')
    except ValueError as e:
        raise ValueError(f"Invalid time format '{time_value}': {e}")


df['formatted_time'] = df['Time'].apply(format_time)
current_time = datetime.now().strftime('%H:%M')

df['is_due'] = df['formatted_time'].apply(lambda x: current_time >= x)


def sound():
    pygame.mixer.init()
    pygame.mixer.music.load('speechfile.mp3')
    pygame.mixer.music.play()
    time.sleep(1)
    pygame.mixer.music.stop()


print(df)
while True:
    current_time = datetime.now().strftime('%H:%M')
    df['is_due'] = df['formatted_time'].apply(lambda x: current_time >= x)
    for i in df.index:
        if df.loc[i, 'is_due'] == True:
            sound()
            print(df)
        else:
            pass
    time.sleep(1)
