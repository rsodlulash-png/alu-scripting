#!/usr/bin/python3
"""Recursively fetch all hot post titles from a subreddit."""

import requests


def recurse(subreddit, hot_list=[]):
    """Return all hot post titles recursively."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "ALUStudentAPI/1.0"
    }

    hot_list = list(hot_list)

    def fetch_page(after=None):
        """Fetch a page and recursively fetch subsequent pages."""

        params = {"limit": 100}

        if after:
            params["after"] = after

        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            params=params
        )

        if response.status_code != 200:
            return False

        data = response.json().get("data", {})
        posts = data.get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                hot_list.append(title)

        next_after = data.get("after")

        if next_after:
            return fetch_page(next_after)

        return True

    if not fetch_page():
        return None

    return hot_list if hot_list else None
