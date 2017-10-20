from actor import data_source
from vLogin import GitHub_spider


def getCall(id):
    def theCall(re):
        re['key_word_id']=id
        data_source.insert_request(re)
        print(re)
    return theCall


def doIt():
    allKeys = data_source.get_all_key()
    for key in allKeys:
        keyID = key['id']
        key.pop('id')
        GitHub_spider.GutHub_spider().spide(key, getCall(keyID))
        break
