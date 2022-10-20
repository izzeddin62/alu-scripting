#!/usr/bin/python3
"""get hot post function"""


import json
import requests
import sys


def recurse(subreddit,  hot_list=[], after=None):
    """get top all hot post"""
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
        children = body["data"]["children"]
        newlist = hot_list + [i["data"]["title"] for i in children]
        return recurse(subreddit, newlist, body["data"]["after"])
    else:
        return hot_list
