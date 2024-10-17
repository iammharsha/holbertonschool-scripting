#!/usr/bin/python3
"""
Query Reddit API
Print sorted count
of given keywords
"""
import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    """
    Recursively queries the Reddit API, parses the titles of hot articles,
    and counts occurrences of the given keywords (case-insensitive).

    :param subreddit: The subreddit to query.
    :param word_list: List of keywords to count in the titles.
    :param word_count: Dictionary to store the counts of each keyword
                       (used during recursion).
    :param after: The 'after' parameter for pagination
                  (used to get the next page of results).
    :return: None. Prints the sorted count of keywords.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {
        "User-Agent": "my-subreddit-keyword-counter/0.1"
    }

    params = {
        "limit": 100,  # Maximum allowed number of posts per request
        "after": after
    }

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code == 200:
            if response.headers.get(
                    'Content-Type') == 'application/json; charset=UTF-8':
                data = response.json()
                posts = data['data']['children']
                after = data['data']['after']

                word_list = [word.lower() for word in word_list]

                if word_count is None:
                    word_count = {word: 0 for word in word_list}

                for post in posts:
                    title_words = post['data']['title'].lower().split()
                    for word in word_list:
                        word_count[word] += title_words.count(word)

                if after:
                    return count_words(subreddit, word_list, word_count, after)

                sorted_word_count = sorted(
                    [(word, count) for word, count in word_count.items()
                     if count > 0],
                    key=lambda x: (-x[1], x[0])
                )

                for word, count in sorted_word_count:
                    print(f"{word}: {count}")
            else:
                return
        else:
            return

    except requests.exceptions.RequestException:
        return
