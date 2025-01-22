from datetime import datetime, timedelta

weekdays = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}


def first_weekday(year, month, day):
    first_weekday_of_month = datetime(year, month, 1)
    diffrence_desired_day = (day - first_weekday_of_month.weekday() + 7) % 7
    return first_weekday_of_month + timedelta(days=diffrence_desired_day)


desire = input("Weekday that you'd like to search: ").capitalize()
print(f"{desire} will be in: {first_weekday(2025, 1, weekdays[desire])}")
