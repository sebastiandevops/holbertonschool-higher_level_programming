#!/usr/bin/python3
"""False.unction that returns True if the object is an instance
of, or if the object is an instance of a class
that inherited from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
    Args:
        obj: the object to lookup.
        a_class (obj): class to compare against.
    """
    return isinstance(obj, a_class)
