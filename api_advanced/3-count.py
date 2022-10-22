#!/usr/bin/python3

"""search post function"""

import json
import operator
import requests


def count_words(subreddit, word_list, after=None):
    """get all the keyword count"""

    if len(word_list) == 0:
        print(None)
        return
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    result = requests.get(url,
                          headers=headers,
                          params={"after": after},
                          allow_redirects=False)
    if result.status_code != 200:
        return None
    body = json.loads(result.text)
    if body["data"]["after"] is not None:
        newlist = word_list
        if type(word_list[0]) is str:
            unique = list(dict.fromkeys([i.lower() for i in word_list]))
            newlist = [{"key": i, "count": 0} for i in unique]
        for i in newlist:
            for j in body["data"]["children"]:
                for k in j["data"]["title"].lower().split():
                    if i["key"] == k:
                        i["count"] = i["count"] + 1
        return count_words(subreddit, newlist, body["data"]["after"])
    else:
        newlist = word_list
        if type(word_list[0]) is str:
            unique = list(dict.fromkeys([i.lower() for i in word_list]))
            newlist = [{"key": i, "count": 0} for i in unique]
        for i in newlist:
            for j in body["data"]["children"]:
                for k in j["data"]["title"].lower().split():
                    if i["key"] == k:
                        i["count"] = i["count"] + 1
        key = operator.itemgetter("count", "key")
        sorted_list = sorted(word_list, key=key, reverse=True)
        word_list = sorted_list
        for i in sorted_list:
            if i["count"] > 0:
                print("{}: {}".format(i["key"], i["count"]))
        return
