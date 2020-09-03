#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import sys
    toPrint = dir(hidden_4)
    for i in toPrint[8:]:
        print("{}".format(i))
