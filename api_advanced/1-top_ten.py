#!/usr/bin/python3
"""Print the titles of the first 10 hot posts on a subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "ALUStudentAPI/1.0"
    }

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False,
        params={"limit": 10}
    )

    if response.status_code != 200:
        print("None")
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    if not posts:
        print("None")
        return

    for post in posts[:10]:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
