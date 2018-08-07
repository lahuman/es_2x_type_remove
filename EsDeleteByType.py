#-*- coding: utf-8 -*-
import requests
import json


ES_URL = "http://localhost:9200/{}/{}/{}"
ES_INDEX = "index"
ES_TYPE = "type"
BULK_SIZE = 500000
COMMAND_SEARCH = "/_search?pretty"


def main():
    actions = list()
    for data in get_id()["hits"]["hits"]:
        actions.append('{"delete": {"_id": "'+data["_id"]+'"}}'+"\n")

    with open("id_list.json", 'w') as file:
        file.writelines(actions)


def get_id():
    query = json.dumps({"query":{"match_all":{}},"size":BULK_SIZE, "fields":["_id"]})
    response = requests.get(ES_URL.format(ES_INDEX, ES_TYPE, COMMAND_SEARCH), data=query)
    results = json.loads(response.text)
    return results


if __name__ == "__main__":
    main()