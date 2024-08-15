#!/usr/bin/python3
"""
This module contains a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after='', word_count={}):
    """Recursively counts and prints the occurrences of words in hot post titles."""
    word_list = [word.lower() for word in word_list]
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.word.count:v1.0 (by /u/yourusername)"}
    params = {"after": after}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return
        
        data = response.json().get("data", {})
        after = data.get("after")
        articles = data.get("children", [])
        
        for article in articles:
            title = article.get("data", {}).get("title", "").lower()
            for word in word_list:
                word_count[word] = word_count.get(word, 0) + title.split().count(word)
        
        if after:
            count_words(subreddit, word_list, after, word_count)
        else:
            if word_count:
                sorted_words = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
                for word, count in sorted_words:
                    if count > 0:
                        print(f"{word}: {count}")
    
    except requests.RequestException:
        return

