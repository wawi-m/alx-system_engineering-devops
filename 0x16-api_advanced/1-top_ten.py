#!/usr/bin/python3
'''
Module contains the function top_ten
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''Returns a subreddit's top ten posts'''
    headers = {'User-Agent': 'Lizzie'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        
        data = response.json()
        children = data.get('data', {}).get('children', [])
        
        if not children:
            print(None)
            return
        
        for post in children:
            print(post.get('data', {}).get('title', None))
            
    except requests.RequestException:
        # Catch any network-related errors or bad HTTP responses
        print(None)
    except ValueError:
        # Handle JSON decoding errors
        print(None)


if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
    else:
        print("Usage: ./1-top_ten.py <subreddit>")
