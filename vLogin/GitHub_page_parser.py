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
    def __init__(self, page_content, page_uri):
        self.page_content = page_content
        self.page_uri = page_uri

    def parser(self):
        soup = bs(self.page_content, "html.parser")
        watch_num = soup.find("a", href=self.page_uri + "/watchers").text.strip()
        star_num = soup.find("a", href=self.page_uri + "/stargazers").text.strip()
        fork_num = soup.find("a", href=self.page_uri + "/network").text.strip()
        description = soup.find("span", {
            "class": "col-11 text-gray-dark mr-2",
            "itemprop": "about"
        }).text.strip()
        relative_time = soup.find("relative-time")['datetime']
        return {
            "name": self.page_uri,
            "uri": self.page_uri,
            "watch_num": watch_num,
            "star_num": star_num,
            "fork_num": fork_num,
            "description": description,
            "relative_time": relative_time

        }
