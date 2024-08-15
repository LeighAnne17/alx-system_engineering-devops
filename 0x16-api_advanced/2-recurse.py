#!/usr/bin/python3
"""
This module contains a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API to retrieve the titles of all hot articles
    for a given subreddit and returns them in a list.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.hot.articles:v1.0 (by /u/yourusername)"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            after = data.get("after")
            articles = data.get("children", [])
            
            for article in articles:
                title = article.get("data", {}).get("title")
                if title:
                    hot_list.append(title)
            
            if after:
                # Recursively call the function to fetch the next page
                return recurse(subreddit, hot_list)
            else:
                # Return the list when no more pages are left
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
