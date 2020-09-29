#!/usr/bin/python3
"""Class Rectangle
"""


class Rectangle:
    """empty class Rectangle that defines a rectangle.

    Attributes:
        Not Attributes for now.

    """
    def __init__(self, width=0, height=0):
        """Example of docstring on the __init__ method.

        Args:
            size (int): size of square.

        """
        self.__height = height
        if type(self.__height) != int:
            raise TypeError('height must be an integer')
        if self.__height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        if type(self.__width) != int:
            raise TypeError('width must be an integer')
        if self.__width < 0:
            raise ValueError('width must be >= 0')

    @property
    def width(self):
        """Getter method width of the rectangle.

        Returns:
            width the square.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter width method.

        Args:
            value (int): new width of the square.

        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method of height of the rectangle.

        Returns:
            Height the square.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height method.

        Args:
            value (int): new height of the square.

        """
        if type(value) != int:
            raise TypeError('height must be an integer')
        else:
            self.__height = value
