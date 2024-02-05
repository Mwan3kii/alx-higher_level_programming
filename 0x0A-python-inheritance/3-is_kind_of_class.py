#!/usr/bin/python3
"""This is module checking instance."""


def is_kind_of_class(obj, a_class):
    """Checks the type of object and subclass.

    Args:
        obj: The object to check.
        a_class: The class to check from.

    Returns:
        int: Either true or false depending.
    """
    if type(obj) is a_class:
        return True
    elif issubclass(type(obj), a_class):
        return True
    else:
        return False
