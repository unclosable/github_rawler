def report_worksummary_render(name, workList):
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
    re_content = '<hr><p>' + name + '总预计时间' + str(expectedTimeAll) + '</p>' + re_content
    re_content += '</tbody></table><hr>'
    return re_content


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
