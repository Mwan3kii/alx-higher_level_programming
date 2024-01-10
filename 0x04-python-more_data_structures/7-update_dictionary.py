#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
def print_sorted_dictionary(a_dictionary):
    sort_keys = sorted(a_dictionary.keys())
    for key in sort_keys:
        print("{}: {}".format(key, a_dictionary[key]))
