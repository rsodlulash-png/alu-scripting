#!/usr/bin/python3
"""Query the Reddit API to get a subreddit's subscriber count."""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a subreddit."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "ALUStudentAPI/1.0"
    }

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)

    return 0
