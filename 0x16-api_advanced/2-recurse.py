#!/usr/bin/python3
"""
Queries the Reddit API and returns
a list containing the titles of all hot
articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.
    """
    headers = {"User-Agent": "Python/0.1(Holberton School 0x16 task 2)"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after} if after else {}

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    if not response.ok:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])
    if not children:
        return hot_list if hot_list else None

    for post in children:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
