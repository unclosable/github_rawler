import requests
from bs4 import BeautifulSoup as bs
from multiprocessing.pool import ThreadPool
from vLogin.GitHub_search_url_maker import search_most_starts, detail_page
from vLogin.GitHub_page_parser import search_page_parser
from vLogin.GitHub_virtual_login import get_login_cookies

# l=Java&o=desc&p=1&q=mysql&s=stars&type=Repositories&utf8=✓
search_param = {
    "l": "java",
    "o": "desc",
    "q": "mysql",
    "s": "stars",
    "type": "Repositories",
    "utf8": "✓"
}


def parser(url, cookies, parser):
    # print(url) # totle page
    try:
        page = requests.get(url, cookies=cookies)
        result = parser(page.content).parser()
        print(result)
        for detail in result:
            detail_url = detail_page(detail['URI'])
            print(detail_url)
            detail_page = requests.get(detail_url, cookies=cookies)
    except Exception as e:
        print(e)


cookies = get_login_cookies();
urls = search_most_starts(**search_param)
pool = ThreadPool(processes=5)
for url in urls:
    pool.apply_async(parser, (url, cookies, search_page_parser))
pool.close()
pool.join()
