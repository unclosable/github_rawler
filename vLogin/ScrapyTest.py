from vLogin.GitHub_spider import GutHub_spider

# l=Java&o=desc&p=1&q=mysql&s=stars&type=Repositories&utf8=✓
search_param = {
    "l": "java",
    "o": "desc",
    "q": "android+animation",
    "s": "stars",
    "type": "Repositories",
    "utf8": "✓"
}


def reCall(re):
    print(re)


the_spider = GutHub_spider()
the_spider.spide(search_param, reCall)
