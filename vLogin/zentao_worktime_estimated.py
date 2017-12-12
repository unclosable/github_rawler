import datetime


def get_thisWeek_workTime():
    now = datetime.datetime.now()
    now_week = now.weekday()
    print(now_week)
    return (now_week + 1) * 8


def get_lastWeek_workTime():
    return 5 * 8


def get_lastMonth_wokeTime():
    now = datetime.datetime.now()
    month = now.month - 1
    year = now.year
    if month == 0:
        month = 12
        year -= 1
    workday = 0
    day = datetime.date(year=year, month=month, day=1)
    while day.month == month:
        if day.weekday() < 5:
            workday += 1
        day = day + datetime.timedelta(days=1)
    return workday * 8


def get_thisMonth_wokeTime():
    now = datetime.datetime.now()
    month = now.month
    year = now.year
    workday = 0
    day = datetime.date(year=year, month=month, day=1)
    while day.month == month:
        if day.weekday() < 5:
            workday += 1
        day = day + datetime.timedelta(days=1)
    return workday * 8