#!/usr/bin/python3
"""
This is a square class.

It defines a class with private attribute size.
"""


class Square:
    """This is a Square class.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        This initilizes a instance size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
