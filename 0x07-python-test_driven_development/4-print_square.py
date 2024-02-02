#!/usr/bin/python3
"""This function prints size of square.
"""


def print_square(size):
    """This prints square size by character.

    Args:
        size (int): The size of square.

    Raises:
        TypeError: size must be an integer.
        ValueError: size must be >= 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
