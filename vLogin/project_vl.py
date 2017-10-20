import requests
from vLogin.zentao_search_url_maker import get_search_url_this_week
from vLogin.zentao_vl import login
from vLogin.zentao_page_parser import report_worksummary
from vLogin.zentao_mail import _smtp_msg

def action():
    cookie = login("songkai", "4a28484c16b6ae56a24308b43c007339")
    query_page_url = get_search_url_this_week()
    query_page = requests.get(query_page_url, cookies=cookie)
    rw = report_worksummary(query_page.content)
    print(rw)

    title = "本周工作报表"
    content = ""
    for name, workList in rw.items():
        content += "<hr>"
        content += name + ":  <br>"
        expectedTimeAll = 0
        for work in workList:
            content += work["workName"] + " [预估用时" + work["expectedTime"] + "]<br>"
            expectedTimeAll += float(work["expectedTime"])
        content += "总用时" + str(expectedTimeAll)
    _smtp_msg(title,content)


if __name__ == "__main__":
    action()
