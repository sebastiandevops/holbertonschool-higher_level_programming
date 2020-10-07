#!/usr/bin/python3
"""Class BaseGeometry
"""


class BaseGeometry:
    """empty class BaseGeometry

    Attributes:
        Not Attributes for now.

    """
    def __init__(self):
        """Init method.

        Args:
            None for now.

        """
        pass

    def area(self):
        """Area method.

        Args:
            None for now.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value.

        Args:
            name (string): name of the object.
            value (int): value to validate.

        """
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')


"""Class Rectangle
"""


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry

    Attributes:
        Not for now.

    """
    def __init__(self, width, height):
        """Init method.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.

        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method to ger the rectangle area.

        Returns:
            Area of the rectangle.

        """
        return self.__width * self.__height

    def __str__(self):
        """repr method.

        Args:
            None

        """
        return "[%s] %d/%d" % (__class__.__name__, self.__width, self.__height)


"""Class Rectangle
"""


class Square(Rectangle):
    """class Rectangle that inherits from BaseGeometry

    Attributes:
        Not for now.

    """
    def __init__(self, size):
        """Init method.

        Args:
            size (int): size of the Square.

        """

        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Method to ger the rectangle area.

        Returns:
            Area of the rectangle.

        """
        return self.__size * self.__size

    def __str__(self):
        """repr method.

        Args:
            None

        """
        return "[%s] %d/%d" % (__class__.__name__,
                               self.__size, self.__size)
