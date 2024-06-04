#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""


def number_of_subscribers(subreddit):
    """Write a function that queries the Reddit API an
    returns the number of subscribers (not active users,
    total subscribers) for a given subreddit. If an
    invalid subreddit is given, the function should return 0."""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
