#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            r = requests.post('http://0.0.0.0:5000/search_user',
                              data={'q': sys.argv[1]})
            r_yeison = r.json()
            print("[{}] {}".format(r_yeison['id'],
                                   r_yeison['name']))
        except KeyError:
            print("No result")
        except Exception:
            print("Not a valid JSON")
    else:
        r = requests.post('http://0.0.0.0:5000/search_user',
                          data={'q': ""})
        print("No result")
