#!/usr/bin/python3

"""search post function"""

import json
import operator
import requests


def count_words(subreddit, word_list, after=None):
    """get all the keyword count"""
    return

    if len(word_list) == 0:
        print(None)
        return
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    result = requests.get(url,
                          headers=headers,
                          params={"after": after},
                          allow_redirects=False)
    listing = []
    if result.status_code != 200:
        return None
    body = json.loads(result.text)
    if body["data"]["after"] is not None:
        newlist = word_list
        if type(word_list[0]) is str:
            unique = [*set([i.lower() for i in word_list])]
            newlist = [{"key": i, "count": 0} for i in unique]
        for i in newlist:
            for j in body["data"]["children"]:
                count = j["data"]["title"].lower().count(i["key"])
                i["count"] = i["count"] + count
        return count_words(subreddit, newlist, body["data"]["after"])
    else:
        sorted_list = sorted(word_list, key=operator.itemgetter("count", "key"))
        sorted_list.reverse()
        for i in sorted_list:
            print("{}: {}".format(i["key"], i["count"]))
        return
