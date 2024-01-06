#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    num = my_list[::-1]
    for i in num:
        print("{:d}".format(i))
