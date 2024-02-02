#!/usr/bin/python3
"""This provides a function for adding two integers.
Example:
    >>> add_integer(2, 4)
    6
"""
def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int): The first one.
        b (int): Second one.
    Raises:
        TypeError: Both integers should be integer or float.

    Returns:
        int: Sum of two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
