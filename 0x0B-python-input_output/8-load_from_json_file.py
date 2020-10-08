#!/usr/bin/python3
""" function that creates an Object from a “JSON file.
"""

import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file"

    Args:
        filename (file): file to read.

    """
    with open(filename, 'r') as f:
        all_lines = f.readlines()
        stri = " "
        stri = stri.join(all_lines)
        return json.loads(stri)
