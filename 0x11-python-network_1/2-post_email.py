#!/usr/bin/python3
"""script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
(decoded in utf-8).
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, data=encoded_data) as response:
        the_page = response.read()
    print(the_page.decode('utf-8'))
