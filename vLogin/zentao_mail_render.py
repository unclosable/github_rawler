def report_worksummary_render(name, workList, totleTime):
    re_content = '<table style="font-family: verdana,arial,sans-serif;' \
                 'font-size:11px;color:#333333;border-width: 1px;' \
                 'border-color: #999999;border-collapse: collapse;">' \
                 '<thread>' \
                 '<th style="background-color:#c3dde0;border-width: 1px;padding: 8px;border-style: solid;border-color: #a9c6c9;">编号</th>' \
                 '<th style="background-color:#c3dde0;border-width: 1px;padding: 8px;border-style: solid;border-color: #a9c6c9;">描述</th>' \
                 '<th style="background-color:#c3dde0;border-width: 1px;padding: 8px;border-style: solid;border-color: #a9c6c9;">预计用时</th>' \
                 '</thread><tbody>'
    expectedTimeAll = 0
    for work in workList:
        re_content += __tmpl_work(work)
        expectedTimeAll += float(work["expectedTime"])
    re_content = '<hr><p>' + name + '总预计时间' + str(expectedTimeAll) + '</p>' + '<hr><p>理论工时：' + str(
        totleTime) + '<p style="color: gray;">理论工时只计算工作日，遇法定节假日请自行减扣</p></p>' + re_content
    re_content += '</tbody></table><hr>'
    return (re_content, expectedTimeAll)


def report_master_worksummary_render(master_subordinate, totleTime):
    re_content = '<table style="font-family: verdana,arial,sans-serif;' \
                 'font-size:11px;color:#333333;border-width: 1px;' \
                 'border-color: #999999;border-collapse: collapse;">' \
                 '<thread>' \
                 '<th style="background-color:#c3dde0;border-width: 1px;padding: 8px;border-style: solid;border-color: #a9c6c9;">姓名</th>' \
                 '<th style="background-color:#c3dde0;border-width: 1px;padding: 8px;border-style: solid;border-color: #a9c6c9;">预计用时</th>' \
                 '</thread><tbody>'
    for name, time in master_subordinate.items():
        re_content += __tmpl_work_master(name, time)
    re_content = '<hr><p>理论工时：' + str(totleTime) + '<p style="color: gray;">理论工时只计算工作日，遇法定节假日请自行减扣</p></p><hr>' + re_content
    re_content += '</tbody></table><hr>'
    return re_content


def __tmpl_work_master(name, time):
    re = '<tr style="background-color:#d4e3e5;">'
    re += '<td style="border-width: 1px;padding: 8px;border-style: solid;border-color: #a9c6c9;">' \
          + name + '</td>'
    re += '<td style="border-width: 1px;padding: 8px;border-style: solid;border-color: #a9c6c9;">' \
          + str(time) + '</td>'
    re += '</tr>'
    return re


def __tmpl_work(work):
    re = '<tr style="background-color:#d4e3e5;">'
    re += '<td style="border-width: 1px;padding: 8px;border-style: solid;border-color: #a9c6c9;">' \
          + work['workID'] + '</td>'
    re += '<td style="border-width: 1px;padding: 8px;border-style: solid;border-color: #a9c6c9;">' \
          + work['workName'] + '</td>'
    re += '<td style="border-width: 1px;padding: 8px;border-style: solid;border-color: #a9c6c9;">' \
          + work['expectedTime'] + '</td>'
    re += '</tr>'
    return re
