#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
to return the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Queries Reddit API to find the number of subscribers in a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:subreddit.subscriber.count:v1.0 (by /u/yourusername)"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get("data", {}).get("subscribers", 0)
        return 0
    except requests.RequestException:
        return 0

