from bs4 import BeautifulSoup as bs


def report_worksummary(content):
    soup = bs(content, "html.parser")
    table = soup.find("table", attrs={
        "id": "worksummary"
    })
    re = {}
    for tr in table.find('tbody').findAll('tr'):
        nameTR = tr.find('td', attrs={
            "class": "w-user"
        })
        if nameTR:
            name = nameTR.text
            tds = tr.findAll('td')[1:]
            i = 0
            jobs = []
            while i < len(tds):
                job = tds[i:i + 11]
                jobs.append({
                    "workName": job[1].text,
                    "workID": job[0].text,
                    "expectedTime": job[8].text,
                    "usedTime": job[9].text
                })
                i += 11
            re[name] = jobs
    return re
