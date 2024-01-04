#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    f = dir()
    for i in range(0, len(f)):
        if f[i][:2] != "__":
            print("{:s}".format(f[i]))
