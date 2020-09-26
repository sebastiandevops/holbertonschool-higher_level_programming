#!/usr/bin/python3
"""function that adds 2 integers,
otherwise raise a TypeError exception
with the message a must be an integer or b must be an integer

"""


def add_integer(a, b=98):
    """Function that adds 2 integers.

    Args:
        a (int): Integer to add
        b (int, optional): Integer to add. Defaults to 98.

    Returns:
        Returns an integer: the addition of a and b.
    """
    if isinstance(a, (float, int)) is False:
        raise TypeError('a must be an integer')
    elif isinstance(b, (float, int)) is False:
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
