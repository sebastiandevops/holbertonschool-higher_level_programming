#!/usr/bin/python3
"""function that prints My name is <first name> <last name>
first_name and last_name must be strings,
otherwise, a TypeError exception is raised with the message
first_name must be a string or last_name must be a string
"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>

    Args:
        first:name (str): first name to print.
        last_name (str): last name to print.

    Returns:
        Name printed.
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
