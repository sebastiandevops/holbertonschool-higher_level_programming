#!/usr/bin/python3
"""script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8).
the script manage urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code
"""
import urllib.request
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode("utf-8", 'ignore'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
