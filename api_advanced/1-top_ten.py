#!/usr/bin/python3
"""
Query Reddit API
to print titles of top 10 hot posts
for a given subreddit
"""

import requests

def top_ten(subreddit):
    """
    Function to print titles of top 10 hot posts in a subreddit

    Args:
        subreddit (string): Name of subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
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
            posts = data['data']['children']

            if posts:
                for post in posts:
                    print(post['data']['title'])
            else:
                print(None)
        else:
            print(None)
    except requests.exceptions.RequestException:
            print(None)

