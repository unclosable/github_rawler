import zySQL

search_param = {
    # "l": "java",
    "o": "desc",
    # "q": "android+animation",
    "s": "stars",
    "type": "Repositories",
    "utf8": "✓"
}


def get_all_key():
    reKeys = []
    re = zySQL.queries.select("id", "key_word", "language").from_("key_word").query()
    for key in re:
        reKey = dict(search_param, **{
            "l": key[2],
            "q": key[1],
            "id": key[0]
        })
        reKeys.append(reKey)
    return reKeys


def insert_request(re):
    insert = zySQL.queries.insert("spider_re",
                                  # id="id",
                                  star_num="star_num",
                                  fork_num="fork_num",
                                  watch_num="watch_num",
                                  uri="uri",
                                  name="name",
                                  relative_time="relative_time",
                                  key_word_id="key_word_id",
                                  description="description",
                                  )
    try:
        insert.do(re)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    get_all_key()
