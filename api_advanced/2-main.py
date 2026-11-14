#!/usr/bin/python3
"""Test the recurse function."""

import sys

if __name__ == "__main__":
    recurse = __import__("2-recurse").recurse

    if len(sys.argv) < 2:
        print("Please pass a subreddit.")
    else:
        result = recurse(sys.argv[1])
        print(result)
