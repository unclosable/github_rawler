from bs4 import BeautifulSoup as bs


def report_worksummary(content):
    soup = bs(content, "html.parser")
    table = soup.find("table", attrs={
        "id": "worksummary"
    })
    # soup.strip()
    re = {}
    last = None
    lastName = None
    for tr in table.find('tbody').findAll('tr'):
        nameTR = tr.find('td', attrs={
            "class": "w-user"
        })
        if nameTR:
            if last:
                re[lastName] = last
            lastName = nameTR.text
            last = []

        tds = tr.findAll('td')
        if nameTR:
            last.append({
                "workName": tds[2].text,
                "workID": tds[1].text,
                "expectedTime": tds[9].text,
                "usedTime": tds[10].text
            })
        else:
            last.append({
                "workName": tds[1].text,
                "workID": tds[0].text,
                "expectedTime": tds[8].text,
                "usedTime": tds[9].text
            })



        # tds = tr.findAll('td')
        # if tds[0].text:
        #     if last:
        #         re[last[0]] = last[1]
        #     last = (tds[0].text, [])
        # last[1].append({
        #     "workName": tds[2].text,
        #     "workID": tds[1].text,
        #     "expectedTime": tds[9].text,
        #     "usedTime": tds[10].text
        # })
    return re
