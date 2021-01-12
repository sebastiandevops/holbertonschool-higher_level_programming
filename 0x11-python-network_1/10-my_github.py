#!/usr/bin/python3
"""script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    url = 'https://api.github.com/' + user
    pw = sys.argv[2]
    r = requests.get(url, auth=(user, pw))
    print(r.json()['id'])
