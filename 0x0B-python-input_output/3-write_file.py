#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
and returns the number of characters written

    Args:
        filename: the file to read.
        text (str): number of lines to read,

    """
    with open(filename, 'w') as f:
        f.write(text)
        return len(text)
