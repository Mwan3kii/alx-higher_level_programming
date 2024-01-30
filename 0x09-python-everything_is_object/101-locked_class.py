#!/usr/bin/python3
"""This is class that prevents objects or attributes."""


class LockedClass:
    """This is a Locked class that prevents user
    from creating new instances attributes.
    """
    __slots__ = ("first_name")
