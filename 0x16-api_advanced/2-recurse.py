#!/usr/bin/python3
"""
Recursive function that querries Reddit API and returns
a list with titles of all hot articles
"""

import requests

def recurse(subreddit, hot_list=[], after= ''):
    req = requests.get( "https://www.reddit.com/r/{}/hot.json".format(subreddit),
    headers={"User-Agent": "Custom"},
    params={"after": after},
    )

    if req.status_code == 200:
    for get_data in req.json().get("data").get("children"):
    dat = get_data.get("data")
    title= dat.get("title")
    hot_list.append(title)
    after = req.json().get("data").get("after")

    if after is None:
        retuen hot_list
    else:
        return recurse(subreddit, hot_list, after)
    else:
        return None
