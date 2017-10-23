import requests
from vLogin.zentao_search_url_maker import get_search_url_report_worksummary_this_week, \
    get_search_url_report_worksummary_last_week
from vLogin.zentao_vl import login
from vLogin.zentao_page_parser import report_worksummary
from vLogin.zentao_mail import _smtp_msg, _receiver_detail, _smtp_msg_receiver
from vLogin.zentao_mail_render import report_worksummary_render


def action():
    cookie = login("songkai", "4a28484c16b6ae56a24308b43c007339")
    query_page_url = get_search_url_report_worksummary_this_week()
    query_page = requests.get(query_page_url, cookies=cookie)
    rw = report_worksummary(query_page.content)
    print(rw)

    title = "本周工作报表"
    # for name, workList in rw.items():
    #     if name in _receiver_detail:
    #         content = ""
    #         content += report_worksummary_render(name, workList)
    #         content += '<br><p style="color: gray;">此邮件为系统自动发布，' \
    #                    '请勿回复，有问题请联系' \
    #                    '<a href="mailto:zhengwei@itiaoling.com" style="color: gray;">系统管理员</a></p>'
    #         _smtp_msg_receiver(title, content, _receiver_detail[name])

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


if __name__ == "__main__":
    action()
