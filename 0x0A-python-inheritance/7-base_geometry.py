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
        if isinstance(value, int) is False:
            raise TypeError(name + ' must be an integer')
        elif value <= 0:
            raise ValueError(name + ' must be greater than 0')
        else:
            return True
