#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    N_arguments = len(sys.argv[1:])
    arguments = sys.argv[1:]
    if N_arguments == 0:
        print("{} arguments.".format(N_arguments))
    elif N_arguments == 1:
        print("{} argument:".format(N_arguments))
    elif N_arguments > 1:
        print("{} arguments:".format(N_arguments))
    for i, item in enumerate(arguments, start=1):
        print("{}: {}".format(i, item))
