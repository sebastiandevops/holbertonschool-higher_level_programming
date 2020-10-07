#!/usr/bin/python3
"""function that adds a new attribute to
an object if it’s possible
Raise a TypeError exception, with the message can't add new
attribute if the object can’t have new attribute
"""


def add_attribute(object, name, value):
    """function that adds a new attribute to
an object if it’s possible
Raise a TypeError exception, with the message can't add new
attribute if the object can’t have new attribute

    Args:
        object: the object to add.
        name (str): name.
        value: value to add.
    """

    if hasattr(object, name) is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(object, name, value)



