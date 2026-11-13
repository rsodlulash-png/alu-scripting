#!/usr/bin/python3
"""Test the top_ten function."""

import sys

if __name__ == "__main__":
    top_ten = __import__("1-top_ten").top_ten

    if len(sys.argv) < 2:
        print("Please pass a subreddit.")
    else:
        top_ten(sys.argv[1])
