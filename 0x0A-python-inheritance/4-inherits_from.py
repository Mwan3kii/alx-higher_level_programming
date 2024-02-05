#!/usr/bin/python3
"""This checks instance of object."""


def inherits_from(obj, a_class):
    """This checks if object is instance of class.

    Args:
        obj: The object.
        a_class: The class.
    Returns:
        int: Either true or false depending.
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
