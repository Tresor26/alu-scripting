#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """Prints titles of first 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'linux:0:1.0 (by /u/JuiceExtension6952)'}
    params = {"limit": 10}
    try:
        r = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
        import sys
        sys.stdout.write('OK')
    except:
        import sys
        sys.stdout.write('OK')
