__basi_url = "https://github.com"
__search_url = __basi_url + "/search?"


def search_most_starts(**agrs):
    requre_url = __search_url
    re = []
    for key, value in agrs.items():
        requre_url += key + "=" + value + "&"
    for i in range(10):
        re.append(requre_url + "p=" + str(i))
    return re


def detail_page(uri):
    return __basi_url + uri
