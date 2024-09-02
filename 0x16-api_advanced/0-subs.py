#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """
    Return number of subscribers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"user-agent": 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    number_of_subscribers = data.get("subscribers")

    return number_of_subscribers
