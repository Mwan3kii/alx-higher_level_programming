#!/usr/bin/python3
"""This module inherits list from class Mylist."""


class MyList(list):
    """This class inherits from list."""
    def print_sorted(self):
        """This prints list in sorted order."""
        new_list = sorted(self)
        print(new_list)
