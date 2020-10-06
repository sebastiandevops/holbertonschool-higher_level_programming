#!/usr/bin/python3
"""Class MyList
"""


class MyList(list):
    """class MyList that inherits from List.

    Attributes:
        Not Attributes for now.

    """
    def print_sorted(self):
        sortedList = self.copy()
        sortedList.sort()
        print(sortedList)
