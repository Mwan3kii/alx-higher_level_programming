#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    num = len(my_list)
    if idx < 0:
        return my_list
    elif idx >= num:
        return my_list
    else:
        new_list = list(my_list)
        new_list[idx] = element
        return new_list
