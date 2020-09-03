#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    for i in range(0, len(arguments)):
        arguments[i] = int(arguments[i])
    print("{}".format(sum(arguments)))
