#!/usr/bin/python3
"""Class MyInt
"""


class MyInt(int):
    """class MyInt that inherits from List.

    Attributes:
        Not Attributes for now.

    """
    def __init__(self, my_int):
        """Rebel function

        Args:
            int (int): integer value.
        """
        self.value = my_int

    def __str__(self):
        """str method.

        Args:
            None

        Retuns:
            Rectangle printed with the print_symbol.

        """
        if self:
            return "%d" % self

    def __eq__(self, other):
        """Setter size method.

        Args:
            other (int): new size of the square.

        """
        return self.value != other

    def __ne__(self, other):
        """Setter size method.

        Args:
            other (int): new size of the square.

        """
        return self.value == other
