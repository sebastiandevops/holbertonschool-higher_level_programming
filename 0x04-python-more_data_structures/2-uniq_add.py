#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqList = []
    if my_list == []:
        print()
    else:
        for i in my_list:
            if i not in uniqList:
                uniqList.append(i)
        return sum(uniqList)
