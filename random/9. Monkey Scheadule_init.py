from datetime import datetime, timedelta

year = 2025
month = 1


def next_day_of_week(start_date, target_weekday):
    days_ahead = target_weekday - start_date.weekday()
    if days_ahead <= 0:  # If target day already passed this week
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


today = datetime.now()
'''
0: Monday
1: Tuesday
2: Wednesday
3: Thursday
4: Friday
5: Saturday
6: Sunday
'''
next_tuesday = next_day_of_week(today, 1)
print("Next Tuesday:", next_tuesday)

# this is finding the next tuesday, not what we looking for but quite well for initiation.
