#!/usr/bin/python3
"""function that writes an Object to a
text file, using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a
text file, using a JSON representation.

    Args:
        my_obj (Object): The object to save to a file.
        filename (file): file to write into..

    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
