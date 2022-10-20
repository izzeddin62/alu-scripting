#!/usr/bin/python3
"""get hot post function"""


import json
import requests
import sys


def recurse(subreddit,  hot_list=[]):
    """get top ten hot post"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=200".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    result = requests.get(url, headers=headers, allow_redirects=False)
    listing = []
    if result.status_code != 200:
        return None
    body = json.loads(result.text)
    if "after" in body["data"]:
        return recurse(subreddit, hot_list + body["data"]["children"])
    else:
        return hot_list
        
