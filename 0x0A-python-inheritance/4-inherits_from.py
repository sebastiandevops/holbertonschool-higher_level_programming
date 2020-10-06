#!/usr/bin/python3
"""function that returns True if the object is an instance of a
class that inherited (directly or indirectly) from the specified
class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a
class that inherited (directly or indirectly) from the specified
class ; otherwise False.
    Args:
        obj: the object to lookup.
        a_class (obj): class to compare against.
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
