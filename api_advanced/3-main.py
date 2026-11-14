#!/usr/bin/python3
"""Test the count_words function."""

import sys

if __name__ == "__main__":
    count_words = __import__("3-count").count_words

    if len(sys.argv) < 2:
        print("Please pass a subreddit.")
    else:
        word_list = [
            "python",
            "java",
            "javascript",
            "c",
            "programming"
        ]

        count_words(sys.argv[1], word_list)
