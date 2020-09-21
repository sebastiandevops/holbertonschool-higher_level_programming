#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter1 = 0
    counter2 = 0
    newList = ""
    try:
        for i in my_list:
            counter2 += 1
        for i in my_list[:x]:
            if type(i) == int:
                newList = newList + str(i)
                counter1 += 1
        num = int(newList)
        print("{:d}".format(num))
        if x > counter2:
            raise IndexError('list index out of range')
        return counter1
    except IndexError:
        raise
