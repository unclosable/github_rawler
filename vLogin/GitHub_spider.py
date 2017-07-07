from vLogin.GitHub_virtual_login import get_login_cookies
import requests
from bs4 import BeautifulSoup as bs
from multiprocessing.pool import ThreadPool
from vLogin.GitHub_search_url_maker import search_most_starts, detail_page
from vLogin.GitHub_page_parser import search_page_parser, detail_page_parser


class GutHub_spider(object):
    def __init__(self):
        self.__vl__ = get_login_cookies()

    def spide(self, search_param, write_call):
        search_urls = search_most_starts(**search_param)
        search_page_parser_pool = ThreadPool(processes=5)
        for search_url in search_urls:
            print(search_url)
            search_page_parser_pool.apply_async(self.__parser_search_page__, (search_url, write_call,))
        search_page_parser_pool.close()
        search_page_parser_pool.join()

    def __parser_search_page__(self, url, write_call):
        try:
            page = requests.get(url, cookies=self.__vl__)
            print(page.content)
            result = search_page_parser(page.content).parser()
            print(result)
            detail_page_parser_pool = ThreadPool(processes=5)
            for detail in result:
                detail_page_parser_pool.apply_async(self.__parser_detail_page__,(detail,write_call,))
        except Exception as e:
            print(e)

    def __parser_detail_page__(self, detail, write_call):
        print(detail)
        detail_url = detail_page(detail['URI'])
        detail_page_content = requests.get(detail_url, cookies=self.__vl__).content
        detail_info = detail_page_parser(detail_page_content, detail['URI']).parser()
        print(detail_info)
        write_call(detail_info)
