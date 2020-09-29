#!/usr/bin/python3
"""Class Rectangle
"""


class Rectangle:
    """empty class Rectangle that defines a rectangle.

    Attributes:
        Not Attributes for now.

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Example of docstring on the __init__ method.

        Args:
            size (int): size of square.

        """
        Rectangle.number_of_instances += 1
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

        Retuns:
            Rectangle printed with the print_symbol.

        """
        stri = ""
        if self.perimeter == 0:
            return stri
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    stri = stri + str(self.print_symbol)
                stri = stri + '\n'
        return "%s" % stri.rstrip()

    def __repr__(self):
        """repr method

        Args:
            None

        Returns:
            a string representation of the rectangle to be
            able to recreate a new instance by using eval().

        """
        return "Rectangle(%d, %d)" % (self.__width, self.__height)

    def __del__(self):
        """Delete method

        Args:
            None

        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare method

        Args:
            Rect_1 (Rectangle): first Rectangle.
            Rect_2 (Rectangle): second Rectangle.

        Returns:
            biggest rectangle based on the area or
            rect_1 if both have the same area value.

        """
        if Rectangle.area(rect_2) > Rectangle.area(rect_1):
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Class method for square.

        Args:
            cls:
            size (int): size of square.

        Returns:
            new Rectangle instance with width == height == size.

        """
        return Rectangle(size, size)
