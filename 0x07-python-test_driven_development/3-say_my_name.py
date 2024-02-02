#!/usr/bin/python3
"""This prints a string."""


def say_my_name(first_name, last_name=""):
    """This prints a string.

    Args:
        first_name (str): The first name.
        last_name (str): The last name.

    Raises:
        TypeError: Fist name and last name must be string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
