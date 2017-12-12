import requests
from vLogin.zentao_search_url_maker import get_search_url_report_worksummary_this_week, \
    get_search_url_report_worksummary_last_week, get_search_url_report_worksummary_this_month
from vLogin.zentao_vl import login
from vLogin.zentao_page_parser import report_worksummary
from vLogin.zentao_mail import _receivers, _receiver_detail, _smtp_msg_receiver
from vLogin.zentao_mail_render import report_worksummary_render, report_master_worksummary_render
from vLogin.zentao_worktime_estimated import get_thisWeek_workTime, get_thisMonth_wokeTime, get_lastWeek_workTime


def action_thisWeek():
    cookie = login("songkai", "4a28484c16b6ae56a24308b43c007339")
    query_page_url = get_search_url_report_worksummary_this_week()
    query_page = requests.get(query_page_url, cookies=cookie)
    rw = report_worksummary(query_page.content)
    title = "本周工作报表"
    for name, mail_address in _receiver_detail.items():
        if name in rw:
            content = ""
            content += report_worksummary_render(name, rw[name])
            content += '<br><p style="color: gray;">此邮件为系统自动发布，' \
                       '请勿回复，有问题请联系' \
                       '<a href="mailto:zhengwei@itiaoling.com" style="color: gray;">系统管理员</a></p>'
            _smtp_msg_receiver(title, content, mail_address)
        else:
            content = "<hr>"
            content += name + "尚无任务记录，请及时补充"
            content += "<hr>"
            content += '<br><p style="color: gray;">此邮件为系统自动发布，' \
                       '请勿回复，有问题请联系' \
                       '<a href="mailto:zhengwei@itiaoling.com" style="color: gray;">系统管理员</a></p>'
            _smtp_msg_receiver(title, content, mail_address)


def action_thisWeek_whitMaster():
    cookie = login("songkai", "4a28484c16b6ae56a24308b43c007339")
    query_page_url = get_search_url_report_worksummary_this_week()
    query_page = requests.get(query_page_url, cookies=cookie)
    rw = report_worksummary(query_page.content)
    worktime = get_thisWeek_workTime()
    title = "本周工作报表"
    for team in _receivers:
        master_email = team['email']
        master_subordinate = {}
        for subordinate in team['subordinate']:
            name = subordinate['name']
            mail_address = subordinate['email']
            if name in rw:
                content = ""
                person_report = report_worksummary_render(name, rw[name], worktime)
                master_subordinate[name] = person_report[1]
                content += person_report[0]
                content += '<br><p style="color: gray;">此邮件为系统自动发布，' \
                           '请勿回复，有问题请联系' \
                           '<a href="mailto:zhengwei@itiaoling.com" style="color: gray;">系统管理员</a></p>'
                _smtp_msg_receiver(title, content, mail_address)
            else:
                master_subordinate[name] = 0
                content = "<hr>"
                content += name + "尚无任务记录，请及时补充"
                content += "<hr>"
                content += '<br><p style="color: gray;">此邮件为系统自动发布，' \
                           '请勿回复，有问题请联系' \
                           '<a href="mailto:zhengwei@itiaoling.com" style="color: gray;">系统管理员</a></p>'
                _smtp_msg_receiver(title, content, mail_address)
        master_content = report_master_worksummary_render(master_subordinate, worktime)
        master_content += "<hr>"
        master_content += '<br><p style="color: gray;">此邮件为系统自动发布，' \
                          '请勿回复，有问题请联系' \
                          '<a href="mailto:zhengwei@itiaoling.com" style="color: gray;">系统管理员</a></p>'
        _smtp_msg_receiver(title, master_content, master_email)


def action_lastWeek():
    cookie = login("songkai", "4a28484c16b6ae56a24308b43c007339")
    query_page_url = get_search_url_report_worksummary_last_week()
    query_page = requests.get(query_page_url, cookies=cookie)
    rw = report_worksummary(query_page.content)
    title = "上周工作总时常"
    for name, mail_address in _receiver_detail.items():
        if name in rw:
            content = ""
            content += report_worksummary_render(name, rw[name])
            content += '<br><p style="color: gray;">此邮件为系统自动发布，' \
                       '请勿回复，有问题请联系' \
                       '<a href="mailto:zhengwei@itiaoling.com" style="color: gray;">系统管理员</a></p>'
            _smtp_msg_receiver(title, content, mail_address)
        else:
            content = "<hr>"
            content += name + "尚无任务记录，请及时补充"
            content += "<hr>"
            content += '<br><p style="color: gray;">此邮件为系统自动发布，' \
                       '请勿回复，有问题请联系' \
                       '<a href="mailto:zhengwei@itiaoling.com" style="color: gray;">系统管理员</a></p>'
            _smtp_msg_receiver(title, content, mail_address)



def action_lastWeek_withMaster():
    cookie = login("songkai", "4a28484c16b6ae56a24308b43c007339")
    query_page_url = get_search_url_report_worksummary_last_week()
    query_page = requests.get(query_page_url, cookies=cookie)
    rw = report_worksummary(query_page.content)
    title = "上周工作总时常"
    worktime = get_lastWeek_workTime()
    for team in _receivers:
        master_email = team['email']
        master_subordinate = {}
        for subordinate in team['subordinate']:
            name = subordinate['name']
            mail_address = subordinate['email']
            if name in rw:
                content = ""
                person_report = report_worksummary_render(name, rw[name], worktime)
                master_subordinate[name] = person_report[1]
                content += person_report[0]
                content += '<br><p style="color: gray;">此邮件为系统自动发布，' \
                           '请勿回复，有问题请联系' \
                           '<a href="mailto:zhengwei@itiaoling.com" style="color: gray;">系统管理员</a></p>'
                _smtp_msg_receiver(title, content, mail_address)
            else:
                master_subordinate[name] = 0
                content = "<hr>"
                content += name + "尚无任务记录，请及时补充"
                content += "<hr>"
                content += '<br><p style="color: gray;">此邮件为系统自动发布，' \
                           '请勿回复，有问题请联系' \
                           '<a href="mailto:zhengwei@itiaoling.com" style="color: gray;">系统管理员</a></p>'
                _smtp_msg_receiver(title, content, mail_address)
        master_content = report_master_worksummary_render(master_subordinate, worktime)
        master_content += "<hr>"
        master_content += '<br><p style="color: gray;">此邮件为系统自动发布，' \
                          '请勿回复，有问题请联系' \
                          '<a href="mailto:zhengwei@itiaoling.com" style="color: gray;">系统管理员</a></p>'
        _smtp_msg_receiver(title, master_content, master_email)


def action_thisMonth():
    cookie = login("songkai", "4a28484c16b6ae56a24308b43c007339")
    query_page_url = get_search_url_report_worksummary_this_month()
    query_page = requests.get(query_page_url, cookies=cookie)
    rw = report_worksummary(query_page.content)
    title = "本月工作报表"
    for name, mail_address in _receiver_detail.items():
        if name in rw:
            content = ""
            content += report_worksummary_render(name, rw[name])
            content += '<br><p style="color: gray;">此邮件为系统自动发布，' \
                       '请勿回复，有问题请联系' \
                       '<a href="mailto:zhengwei@itiaoling.com" style="color: gray;">系统管理员</a></p>'
            _smtp_msg_receiver(title, content, mail_address)
        else:
            content = "<hr>"
            content += name + "尚无任务记录，请及时补充"
            content += "<hr>"
            content += '<br><p style="color: gray;">此邮件为系统自动发布，' \
                       '请勿回复，有问题请联系' \
                       '<a href="mailto:zhengwei@itiaoling.com" style="color: gray;">系统管理员</a></p>'
            _smtp_msg_receiver(title, content, mail_address)


def action_thisMonth_withMaster():
    cookie = login("songkai", "4a28484c16b6ae56a24308b43c007339")
    query_page_url = get_search_url_report_worksummary_this_month()
    query_page = requests.get(query_page_url, cookies=cookie)
    rw = report_worksummary(query_page.content)
    title = "本月工作报表"
    worktime = get_thisMonth_wokeTime()
    for team in _receivers:
        master_email = team['email']
        master_subordinate = {}
        for subordinate in team['subordinate']:
            name = subordinate['name']
            mail_address = subordinate['email']
            if name in rw:
                content = ""
                person_report = report_worksummary_render(name, rw[name], worktime)
                master_subordinate[name] = person_report[1]
                content += person_report[0]
                content += '<br><p style="color: gray;">此邮件为系统自动发布，' \
                           '请勿回复，有问题请联系' \
                           '<a href="mailto:zhengwei@itiaoling.com" style="color: gray;">系统管理员</a></p>'
                _smtp_msg_receiver(title, content, mail_address)
            else:
                master_subordinate[name] = 0
                content = "<hr>"
                content += name + "尚无任务记录，请及时补充"
                content += "<hr>"
                content += '<br><p style="color: gray;">此邮件为系统自动发布，' \
                           '请勿回复，有问题请联系' \
                           '<a href="mailto:zhengwei@itiaoling.com" style="color: gray;">系统管理员</a></p>'
                _smtp_msg_receiver(title, content, mail_address)
        master_content = report_master_worksummary_render(master_subordinate, worktime)
        master_content += "<hr>"
        master_content += '<br><p style="color: gray;">此邮件为系统自动发布，' \
                          '请勿回复，有问题请联系' \
                          '<a href="mailto:zhengwei@itiaoling.com" style="color: gray;">系统管理员</a></p>'
        _smtp_msg_receiver(title, master_content, master_email)
