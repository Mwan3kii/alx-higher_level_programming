#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for elem in range(x):
            value = my_list[elem]
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                count += 1
    except (ValueError, TypeError):
        pass
    print()
    return count
