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

    def from_json_string(my_str):
        """function that returns an object (Python data structure)
        represented by a JSON string.

        Args:
            my_str (str): object to be represented as JSON.

        """
        return json.loads(my_str)
