#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status
using the urllib package.
"""
import urllib.request
import sys


if __name__ == "__main__":
    headers = {}
    req = urllib.request.Request(sys.argv[1], headers=headers)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    print(response.info()["X-Request-Id"])
