#!/usr/bin/python3
"""Class Square
"""
from .base import Base
from .rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle

    Attributes:
        size (int): size of the square
        x (int): x position of the square.
        y (int): y position of the square.
        id (int): id of the square.

    """
    def __init__(self, size, x=0, y=0, id=None):
        """Init method.

        Args:
            size (int): size of the square
            x (int): x position of the square.
            y (int): y position of the square.
            id (int): id of the square.

        """
        if id is None:
            self.id = Base().id
        else:
            self.id = id
        self.__size = size
        if type(self.__size) != int:
            raise TypeError('size must be an integer')
        if self.__size <= 0:
            raise ValueError('size must be > 0')
        self.__x = x
        if type(self.__x) != int:
            raise TypeError('x must be an integer')
        if self.__x < 0:
            raise ValueError('x must be >= 0')
        self.__y = y
        if type(self.__y) != int:
            raise TypeError('y must be an integer')
        if self.__y < 0:
            raise ValueError('y must be >= 0')
        super().__init__(width=size, height=size, x=self.__x,
                         y=self.__y, id=self.id)

    def __str__(self):
        """repr method.

        Args:
            None

        """
        representation = "[Square] (%d) %d/%d - %d" % (self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__size,)
        return representation

    @property
    def size(self):
        """Getter method width of the rectangle.

        Returns:
            width the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter width method.

        Args:
            value (int): new width of the square.

        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__size = value

    def update(self, *args, **kwargs):
        """public method  that assigns an argument to each attribute:
           **kwargs must be skipped if *args exists and is not empty
           Each key in this dictionary represents an attribute to the instance.

            Args:
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute

            kwargs:
                size (int): size of the square.
                x (int): x position of the square.
                y (int): y position of the square.
                id (int): id of the square.

        """
        if len(args) == 0:
            if kwargs.get("id") is not None:
                self.id = kwargs['id']
            if kwargs.get("size") is not None:
                self.__size = kwargs['size']
            if kwargs.get("x") is not None:
                self.__x = kwargs['x']
            if kwargs.get("y") is not None:
                self.__y = kwargs['y']
        else:
            self.id = args[0]
            if len(args) > 1:
                self.__size = args[1]
            if len(args) > 2:
                self.__x = args[2]
            if len(args) > 3:
                self.__y = args[3]

    def to_dictionary(self):
        """Public method that returns the dictionary
        representation of a Square
        """
        dictionary = self.__dict__
        emptyDict = {}
        emptyDict['size'] = dictionary['_Square__size']
        emptyDict['x'] = dictionary['_Square__x']
        emptyDict['y'] = dictionary['_Square__y']
        return emptyDict
