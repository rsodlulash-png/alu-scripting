#!/usr/bin/python3
"""Count keywords in hot Reddit post titles recursively."""

import requests


def count_words(subreddit, word_list, after=None,
                keyword_counts=None, post_counts=None):
    """Recursively count and print keyword occurrences."""

    if keyword_counts is None:
        keyword_counts = {}

        for word in word_list:
            word = word.lower()
            if word:
                keyword_counts[word] = (
                    keyword_counts.get(word, 0) + 1
                )

        post_counts = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "ALUStudentAPI/1.0"
    }

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
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "")

        for word in title.lower().split():
            if word in keyword_counts:
                post_counts[word] = post_counts.get(word, 0) + 1

    next_after = data.get("after")

    if next_after:
        return count_words(
            subreddit,
            word_list,
            next_after,
            keyword_counts,
            post_counts
        )

    results = []

    for word, multiplier in keyword_counts.items():
        count = post_counts.get(word, 0) * multiplier

        if count > 0:
            results.append((word, count))

    results.sort(key=lambda item: (-item[1], item[0]))

    for word, count in results:
        print("{}: {}".format(word, count))
