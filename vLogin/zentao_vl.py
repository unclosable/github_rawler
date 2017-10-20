import requests
from bs4 import BeautifulSoup as bs
import re

base_header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,la;q=0.2",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}


def login(account, password):
    # 访问
    index = requests.get("http://project.itiaoling.com/zentao/index.html")
    cookies = index.cookies
    # 跳转登录页面URL
    login_url = "http://project.itiaoling.com" + re.search('location=\'(.+)\'', bytes.decode(index.content)).group(1)
    # 访问登录页面
    login_page = requests.get(login_url, cookies=cookies)
    cookies = index.cookies
    soup = bs(login_page.content, "html.parser")
    # 获取禅道认证地址
    iframe = soup.find("iframe", attrs={
        "id": "updater"
    })
    # 访问禅道认证地址
    updaterpage = requests.get(iframe['src'], {
        "lang": "zh_cn"
    }, headers=dict(base_header, **{
        "Referer": login_url
    }))
    cookies = updaterpage.cookies
    # 提交登陆信息
    logined = requests.post(login_url, {
        "account": account,
        "password": password
        # "account": "songkai",
        # "password": "4a28484c16b6ae56a24308b43c007339"
    }, cookies=cookies)
    cookies = logined.cookies

    return cookies
