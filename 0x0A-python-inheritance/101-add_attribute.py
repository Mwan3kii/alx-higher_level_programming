#!/usr/bin/python3
"""Adds a new attribute to object."""


def add_attribute(obj, attribute, value):
    """Adds new attribute to object.

    Args:
        obj: Object to add.
        attribute: The attr to add.
        value: Valur to assign to.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[attribute] = value
