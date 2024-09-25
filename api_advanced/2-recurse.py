#!/usr/bin/python3
"""
Query Reddit API
returns a list containing the titles of all hot articles
for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Function to print titles of top 10 hot posts in a subreddit

    Args:
        subreddit (string): Name of subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Harsha"
    }
    params = {
        "limit": 100,
        "after": after
    }
    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
        )

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            hot_list.extend([post['data']['title'] for post in posts])
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.exceptions.RequestException:
        return None
