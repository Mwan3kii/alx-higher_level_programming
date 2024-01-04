#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    f = dir(hidden_4)
    for i in range(0, len(f)):
        if f[i][:2] == "__":
            continue
        print("{:s}".format(f[i]))
