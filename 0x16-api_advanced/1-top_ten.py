#!/usr/bin/python3
"""
Queries the API and returns the number of total subscribers for a given
subreddit.
"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python/task 1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            top_data = response.json()["data"]["children"]
            for post in top_data:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
    except Exception as e:
        print(None)
