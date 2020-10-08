#!/usr/bin/python3
"""function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and
boolean) for JSON serialization of an object.
"""


def class_to_json(obj):
    """function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and
boolean) for JSON serialization of an object.

    Args:
        obj (Object): The object to save to a class.

    """
    return obj.__dict__
