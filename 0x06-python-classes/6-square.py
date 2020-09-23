#!/usr/bin/python3
"""Class Square
"""


class Square:
    """empty class Square that defines a square.

    Attributes:
        Not Attributes for now.

    """
    def __init__(self, size=0, position=(0, 0)):
        """Example of docstring on the __init__ method.

        Args:
            size (int): size of square.
            position (tuple): position of square

        """
        self.__size = size
        if type(self.__size) != int:
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')
        self.__position = position
        m = 'position must be a tuple of 2 positive integers'
        if type(self.__position) != tuple or len(self.__position) != 2:
            raise TypeError(m)
        for element in self.__position:
            if type(element) != int or element < 0:
                raise TypeError(m)

    def area(self):
        """Class methods are similar to regular functions.

        Returns:
            Area of the square.

        """
        return self.__size * self.__size

    @property
    def size(self):
        """Class methods are similar to regular functions.

        Returns:
            Size the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter size method.

        Args:
            value (int): new size of the square.

        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #.add()

        """
        if self.__size == 0:
            print()
        else:
            for j in range(self.__size + self.__position[1]):
                if j < self.__position[1]:
                    print()
                else:
                    for i in range(self.__size + self.__position[0]):
                        if i < self.__position[0]:
                            print(" ", end='')
                        else:
                            print("#", end='')
                    print()

    @property
    def position(self):
        """Property to retrive the position.

        Returns:
            Position of the square.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter position method.

        Args:
            value (int): new position of the square.

        """
        m = 'position must be a tuple of 2 positive integers'
        if type(self.__position) != tuple or len(self.__position) != 2:
            raise TypeError(m)
        for element in self.__position:
            if type(element) != int or element < 0:
                raise TypeError(m)
        else:
            self.__size = value
