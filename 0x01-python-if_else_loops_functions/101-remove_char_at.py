#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    if len(str) > n:
        newStr = str[0:n:] + str[n + 1::]
        return newStr
    else:
        return str
