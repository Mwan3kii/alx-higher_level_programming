#!/usr/bin/python3
"""This checks if instace is in class."""


def is_same_class(obj, a_class):
    """This checks is ogject is an instance of class.

    Args:
        obj: The object to check.
        a_class: The class to check from.
    Returns:
        int: Either true or false depending.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
