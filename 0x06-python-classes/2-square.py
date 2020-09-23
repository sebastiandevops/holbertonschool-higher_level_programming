#!/usr/bin/python3
"""Class Square
"""


class Square:
    """empty class Square that defines a square.

    Attributes:
        Not Attributes for now.

    """
    def __init__(self, size=0):
        """Example of docstring on the __init__ method.

        Args:
            size (int): size of square.

        """
        self.__size = size
        if type(self.__size) != int:
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')
