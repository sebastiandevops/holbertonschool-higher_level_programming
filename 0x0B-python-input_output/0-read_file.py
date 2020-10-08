#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout.

    Args:
        filename: the file to read.

    """
    with open(filename, 'r') as f:
        print(f.read(), end='')
