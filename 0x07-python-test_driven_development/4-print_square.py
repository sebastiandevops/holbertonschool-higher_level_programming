#!/usr/bin/python3
"""function that prints a square with the character #.
size must be an integer,
otherwise raise a TypeError exception
with the message size must be an integer
if size is less than 0,
raise a ValueError exception with the message size must be >= 0
if size is a float and is less than 0,
raise a TypeError exception with the message size must be an integer
"""


def print_square(size):
    """function that prints a square with the character #.

    Args:
        size (int): length of the square.

    Returns:
        Square printed.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print(size * "#")
