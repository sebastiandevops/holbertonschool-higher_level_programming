#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter1 = 0
    counter2 = 0
    newList = ""
    try:

        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                counter1 += 1
        print()
        return counter1
    except IndexError:
        raise
