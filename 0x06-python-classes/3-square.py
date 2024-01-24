#!/usr/bin/python3
"""
This is a Square class.

It defines a private instance attribute.
"""


class Square:
    """
    This is a square class.

    Attributes:
        __ size (int): the size of the square.
    """
    def __init__(self, size=0):
        """
        the init method initializes the size of square

        Args:
            size (int): the size of the square
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

    def area(self):
        """
        Does area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2
