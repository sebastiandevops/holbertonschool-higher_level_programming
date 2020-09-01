#!/usr/bin/python3
def uppercase(str):
    for char in range(0, len(str)):
        letter = ord(str[char])
        if letter >= 97 and letter <= 122:
            letter -= 32
        newString = chr(letter)
        print("{}".format(newString), end="")
    print('')
