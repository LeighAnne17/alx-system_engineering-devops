#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after="", word_count={}):
    # Convert all words in the word_list to lowercase
    word_list = [word.lower() for word in word_list]
    
    # Define the Reddit API URL
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditApp/0.1 (contact: your_email@example.com)"}
    params = {"after": after}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code != 200:
            return
        
        # Parse the response JSON data
        data = response.json().get("data", {})
        after = data.get("after", None)
        articles = data.get("children", [])
        
        # Loop through each article
        for article in articles:
            title = article.get("data", {}).get("title", "").lower()
            
            # Count occurrences of each word in the title
            for word in word_list:
                word_count[word] = word_count.get(word, 0) + title.split().count(word)
        
        # Recursively call the function if there are more pages
        if after is not None:
            count_words(subreddit, word_list, after, word_count)
        else:
            # Sort and print the results
            if word_count:
                sorted_words = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
                for word, count in sorted_words:
                    if count > 0:
                        print(f"{word}: {count}")
    
    except requests.exceptions.RequestException:
        return


