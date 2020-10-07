#!/usr/bin/python3
"""Class MyInt
"""


class MyInt(int):
    """class MyInt that inherits from List.

    Attributes:
        Not Attributes for now.

    """
    def __str__(self):
        """str method.

        Args:
            None

        Retuns:
            Rectangle printed with the print_symbol.

        """
        if self:
            return "%d" % self
        if self == self.__class__:
            return "%s" % True
        else:
            return "%s" % False
