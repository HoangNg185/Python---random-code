'''import time
from datetime import datetime, timedelta
import calendar
import pandas as pd

weekdays={'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
weekdays_rev={v:k for k,v in weekdays.items()}

def first_weekday(year,month,day):
    first_weekday_of_month=datetime(year,month,1)
    diffrence_desired_day=(day-first_weekday_of_month.weekday()+7)%7
    return first_weekday_of_month+timedelta(days=diffrence_desired_day)

desire='Tuesday'
desire_1=first_weekday(2025, 1, weekdays[desire])
print(f"{desire} will be in: {desire_1}")
desire_2=desire_1+timedelta(days=7)
print(f"{weekdays_rev[desire_2.weekday()]}: {desire_2}")
desire_3=desire_1+timedelta(days=14)
desire_4=desire_1+timedelta(days=21)


dates=[desire_1, desire_2, desire_3, desire_4]
ext=[1,3,4]
if len(dates)<=28:
    for i in ext:
        for j in dates:
            dates.append(j+timedelta(days=i))
            if len(dates)>28:
                break

df=pd.DataFrame({'Date': dates})

for i in df.index:
    df.loc[i,'Weekday']=weekdays_rev[df.loc[i,'Date'].weekday()][0:3]
df=df.sort_values(by='Date')
print(df.to_string())'''

# i started to find the date of a tuesday, then find next tuesday, then +1+3+4 to find other chosen weekdays but the result was duplicated. Another idea is i just import all the date of that month, paste the default scheadule of tue,wed,fri,sat. other day would leave NA, then use drop NA so we only have the desire predict scheadule. fuk me.

import calendar
from datetime import datetime

import pandas as pd

year, month = 2025, 1
month_length = calendar.monthrange(year, month)[1]
print(month_length)

weekdays = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
start = {1: '10:45', 2: '10:45', 4: '10:00', 5: '10:00', 0: None, 3: None, 6: None}
end = {1: '11:00', 2: '11:00', 4: '8:00', 5: '8:00', 0: None, 3: None, 6: None}
breakk = {1: '1:00', 0: '0:00', 2: '0:00', 3: '0:00', 4: '0:00', 5: '0:00', 6: '0:00', }

dates = []
for i in range(1, month_length + 1):
    dates.append(datetime(year, month, i))
df = pd.DataFrame({'Date': dates})
for i in df.index:
    df.loc[i, 'Weekday'] = weekdays[df.loc[i, 'Date'].weekday()][0:3]
    df.loc[i, 'start'] = start[df.loc[i, 'Date'].weekday()]
    df.loc[i, 'end'] = end[df.loc[i, 'Date'].weekday()]
    df.loc[i, 'break'] = breakk[df.loc[i, 'Date'].weekday()]
df['start'] = pd.to_datetime(df['start'], format='%H:%M')
df['end'] = pd.to_datetime(df['end'], format='%H:%M')
df['break'] = pd.to_datetime(df['break'], format='%H:%M')
df['separate'] = '12:00'
df['separate'] = pd.to_datetime(df['separate'], format='%H:%M')

df['total'] = df['end'] + df['separate'] - df['start'] - df['end']
df = df.dropna()

df.to_csv('Outputs\\monkey_new.csv')
print(df.to_string())
print(df.dtypes)
# still has problem with non-time-factor in those cells
