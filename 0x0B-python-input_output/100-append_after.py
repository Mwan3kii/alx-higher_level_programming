#!/usr/bin/python3
"""Inserts a line text to file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line text file.

    Args:
        filename: The filename.
        search_string: The search string.
        new_string: The new string.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line and new_string not in lines:
                file.write(new_string)
