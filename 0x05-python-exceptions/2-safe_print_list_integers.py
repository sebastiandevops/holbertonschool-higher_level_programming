#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    new_list = []
    for value in my_list:
        try:
            new_list.append(int(value))
        except ValueError:
            continue
