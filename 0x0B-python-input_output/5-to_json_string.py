#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)

    Args:
        my_obj (str): object to be represented as JSON.

    """
    return json.dumps(my_obj)
