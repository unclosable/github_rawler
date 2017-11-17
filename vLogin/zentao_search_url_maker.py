import time, datetime, calendar

__basi_url = "http://project.itiaoling.com"
__search_url = __basi_url + "/zentao/report-worksummary-%s-%s-13.html"


def get_search_url_report_worksummary_this_week():
    now = datetime.datetime.now()
    now_week = now.weekday()
    first = now + datetime.timedelta(days=-now_week)
    last = now + datetime.timedelta(days=6 - now_week)
    firstStr = first.strftime('%Y%m%d')
    lastStr = last.strftime('%Y%m%d')
    return __search_url % (firstStr, lastStr)


def get_search_url_report_worksummary_last_week():
    now = datetime.datetime.now()
    now_week = now.weekday()
    first = now + datetime.timedelta(days=-7 - now_week)
    last = now + datetime.timedelta(days= - now_week)
    firstStr = first.strftime('%Y%m%d')
    lastStr = last.strftime('%Y%m%d')
    return __search_url % (firstStr, lastStr)


def get_search_url_report_worksummary_this_month():
    now = datetime.datetime.now()
    month=now.month
    year=now.year
    # 获取当月第一天的星期和当月的总天数
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)
    # 获取当月的第一天
    firstDay = datetime.date(year=year, month=month, day=1).strftime('%Y%m%d')
    lastDay = datetime.date(year=year, month=month, day=monthRange).strftime('%Y%m%d')
    return __search_url % (firstDay, lastDay)
