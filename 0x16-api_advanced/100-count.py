#!/usr/bin/python3
"""
Recursively queries the Reddit API, parses the titles of all hot articles,
and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API,
    parses the titles of all hot articles,
    and prints a sorted count of given keywords.
    """
    if not word_list:
        return

    headers = {"User-Agent": "Python/0.1(Holberton School 0x16 task 100)"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after} if after else {}

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    if not response.ok:
        print(None)
        return

    data = response.json().get("data", {})
    children = data.get("children", [])
    if not children:
        if not word_count:
            print(None)
        else:
            sorted_word_count = sorted(word_count.items(),
                                       key=lambda x: (-x[1],
                                       x[0]))
            for word, count in sorted_word_count:
                print(f"{word}: {count}")
        return

    for post in children:
        title = post.get("data", {}).get("title", "").lower()
        for word in word_list:
            word = word.lower()
            if word in title.split():
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    after = data.get("after")
    count_words(subreddit, word_list, after, word_count)
