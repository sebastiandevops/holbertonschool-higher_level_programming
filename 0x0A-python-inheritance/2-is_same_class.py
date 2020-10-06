#!/usr/bin/python3
"""Function that returns True if the object
is exactly an instance of the specified class;
otherwise False.
"""


def is_same_class(obj, a_class):
    """Function that returns True if the object
is exactly an instance of the specified class;
otherwise False.

    Args:
        obj: the object to lookup.
        a_class (obj): class to compare against.
    """
    if a_class == object:
        return False
    else:
        return isinstance(obj, a_class)
