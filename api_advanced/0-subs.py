#!/usr/bin/python3
"""
Query Reddit API
to return number of subscribers
in a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function to get number of subscribers in a subreddit

    Args:
        subreddit (string): Name of subreddit

    Returns:
        int: Number of subscribers,
             0 if invalid subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Harsha"
    }
    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
        )
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.exceptions.JSONDecodeError:
        return 0
