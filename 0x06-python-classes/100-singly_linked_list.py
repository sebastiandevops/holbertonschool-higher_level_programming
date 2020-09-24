#!/usr/bin/python3
"""Class Node
"""


class Node:
    """class Node that defines a node of a singly linked list

    Attributes:
        Not Attributes for now.

    """
    def __init__(self, data, next_node=None):
        """Example of docstring on the __init__ method.

        Args:
            data: Private instance attribute.
            next_node: node of a singly linked list.

        """
        self.__data = data
        if type(self.__data) != int:
            raise TypeError('data must be an integer')
        self.__next_node = next_node
        if type(self.__next_node) != Node:
            raise TypeError('next_node must be a Node object')

    @property
    def data(self):
        """Class methods are similar to regular functions.

        Returns:
            data of list.

        """
        return self.__data

    @data.setter
    def data(self, value):
        """Setter data method.

        Args:
            value (int): new data of the linked list.

        """
        if type(value) != int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """Class methods are similar to regular functions.

        Returns:
            next_node of list.

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter data method.

        Args:
            value (int): new data of the linked list.

        """
        if type(value) != Node:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


"""Class SingleLinkedList
"""


class SinglyLinkedList:
    """class SinglyLinkedList that defines a singly linked list

    Attributes:
        Head: Private instance attribute

    """
    def __init__(self):
        """Example of docstring on the __init__ method.

        Args:
            head: The head of the list.

        """
        self.__head = None

    def sorted_insert(self, value):
        """sorted insert method.

        Args:
            value (int): new data of the linked list.

        """
        new_node = Node(value)
        if(self.__head):
            current = self.__head
            while(current.__next_node):
                current = current.__next_node
            current.__next_node = new_node
        else:
            self.__head = new_node

    def print(self):
        """Printed method.

        Args:
            Not for now.

        """
        current = self.__head
        while current:
            print(current.__data)
            current = current.__next_node
