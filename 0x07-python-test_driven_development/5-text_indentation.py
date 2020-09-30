#!/usr/bin/python3
"""function that prints a text with 2 new lines after
each of these iacters: ., ? and :
text must be a string, otherwise raise a TypeError exception
with the message text must be a string
"""


def text_indentation(text):
    """function that prints a text with 2 new lines after
    each of these iacters: ., ? and :

    Args:
        text (str): text to print indented.

    Returns:
        Text printed.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        stri = " ".join(text.split())
        for i in range(len(stri)):
            if i == len(stri) - 1:
                break
            if i == 0:
                print("{}{}".format(stri[i].lstrip(), stri[i + 1].lstrip()), end='')
            elif stri[i] == ".":
                print()
                print()
                print(stri[i + 1].lstrip(), end='')
            elif stri[i] == '?':
                print()
                print()
                print(stri[i + 1].lstrip(), end='')
            elif stri[i] == ':':
                print()
                print()
                print(stri[i + 1].lstrip(), end='')
            else:
                print(stri[i + 1], end='')
