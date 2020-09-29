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

    def area(self):
        """Method to ger the rectangle area.

        Returns:
            Area of the rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """Method to ger the rectangle perimeter.

        Returns:
            Perimeter of the rectangle.

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """repr method.

        Args:
            None

        """
        stri = ""
        if self.perimeter == 0:
            return stri
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    stri = stri + "#"
                stri = stri + '\n'
        return "%s" % stri.rstrip()

    def __repr__(self):
        """repr method

        Args:
            None

        """
        return "Rectangle(%d, %d)" % (self.__width, self.__height)

    def __del__(self):
        """Delete method

        Args:
            None

        """
        print("Bye rectangle...")
