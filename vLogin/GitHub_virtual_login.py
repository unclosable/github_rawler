import requests
from bs4 import BeautifulSoup as bs

__login_url = "https://github.com/login"
__login_action = "https://github.com/session"


def get_login_cookies():
    login_page = requests.get(__login_url)
    cookies = login_page.cookies
    soup = bs(login_page.content, "html.parser")
    authenticity_token = soup.find('input', {
        "name": "authenticity_token"
    })['value']
    logined = requests.post(__login_action, {
        "authenticity_token": authenticity_token,
        "login": "unclosable",
        "password": "zw19890603"
    }, cookies=cookies)

    cookies = logined.cookies
    return cookies
