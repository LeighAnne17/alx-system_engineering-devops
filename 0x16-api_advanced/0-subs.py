#!/usr/bin/python3
"""
queries the api and returns number of subs for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Reddit-API-Checker/0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    else:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
        return 0
