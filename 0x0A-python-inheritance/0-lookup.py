#!/usr/bin/python3
"""This module returns a list of attributes and methods of object."""


def lookup(obj):
    """This returns attributes and methods.

    Returns:
        obj: list of obj.
    """
    return (dir(obj))
