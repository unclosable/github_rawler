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
