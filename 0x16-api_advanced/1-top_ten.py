#!/usr/bin/python3
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Reddit-API-Checker/0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        # Parsing the JSON response
        posts = response.json().get("data", {}).get("children", [])

        if not posts:
            print("None")
            return

        for post in posts:
            print(post.get("data", {}).get("title"))

    except requests.exceptions.HTTPError:
        print("None")
    except Exception as err:
        print("None")

