#!/usr/bin/python3
import requests

"""
queries the reddit api and returns the number
of total subscribers for the subreddit
"""


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {"User-Agent": "python/(hoberton school task 16)/0.1"}

    response = requests.get(url, headers=header)
    if response.ok:
        subscribers_count = response.json().get("data").get("subscribers")
        return subscribers_count
    else:
        return 0
