from bs4 import BeautifulSoup as bs


class search_page_parser(object):
    def __init__(self, page_content):
        self.page_content = page_content

    def parser(self):
        re = []
        soup = bs(self.page_content, "html.parser")
        all_div = soup.find_all("div", {
            "class": "repo-list-item d-flex flex-justify-start py-4 public source"
        })
        for div in all_div:
            add_re = {}
            add_re['name'] = div.find("a", class_="v-align-middle").text
            add_re['URI'] = div.find("a", class_="v-align-middle")["href"]
            re.append(add_re)
        return re


class detail_page_parser(object):
    def __init__(self, page_content):
        self.page_content = page_content

    def parser(self):
        # re = []
        soup = bs(self.page_content, "html.parser")
        # all_div = soup.find_all("div", {
        #     "class": "repo-list-item d-flex flex-justify-start py-4 public source"
        # })
        print(soup.prettify())
