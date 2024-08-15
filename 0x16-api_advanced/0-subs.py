#!/usr/bin/python3
"""
queries the api and returns number of subs for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subcribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
