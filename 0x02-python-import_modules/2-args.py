#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = len(argv) - 1
    if args < 1:
        print("{} arguments.".format(args))
    elif args == 1:
        print("{} argument:".format(args))
    else:
        print("{} argments:".format(args))
    for i in range(1, args + 1):
        print("{}: {:s}".format(i, argv[i]))
