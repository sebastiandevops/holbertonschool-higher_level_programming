#!/usr/bin/python3
"""Base module
"""
import json


class Base:
    """Base

    Attrs:
        nb_objects (int): private attribute that
        indicates the number of objects.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Init method.

        Args:
            id (str):  public instance attribute that identifies the object.

        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method  that returns the JSON
        string representation of list_dictionaries

        Args:
            list_dictionaries (list): List of dictionaries.

        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """function tthat writes the JSON
        string representation of list_objs to a file.

        Args:
            cls (class): class of the object.
            list_objs (list): list of instances who inherits of Base.
            example: list of Rectangle or list of Square instances.

        """
        filename = cls.__name__
        listDict = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                listDict.append(dictionary)
        jstring = cls.to_json_string(listDict)
        with open(filename+".json", 'w') as f:
            f.write(jstring)

    def from_json_string(json_string):
        """fstatic method that returns the list of the
        JSON string representation json_string.

        Args:
            json_string (str): object to be represented as JSON.

        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns an instance with
        all attributes already set.

        Args:
            dictionary: can be thought of as a double pointer to a dictionary.

        """
        if cls.__name__ == "Rectangle":
            rectangle = cls(1, 1, 1, 1)
            rectangle.update(**dictionary)
            return rectangle
        elif cls.__name__ == "Square":
            square = cls(1, 1, 1, 1)
            square.update(**dictionary)
            return square

    @classmethod
    def load_from_file(cls):
        """ Class method that that returns a list of instances

        Args:
            filename (file): file to read.

        """
        with open(cls, 'r') as f:
            all_lines = f.readlines()
            stri = " "
            stri = stri.join(all_lines)
            return json.loads(stri)
