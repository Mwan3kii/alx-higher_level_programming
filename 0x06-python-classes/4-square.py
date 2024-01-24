#!/usr/bin/python3
"""
This is a square class.

It defines a private instance attribute.
"""
class Square:
    """
    This is a square class.

    Attributes:
        size (int): size of the square.
    """
    def __init__(self, size=0):
        """
        init method initializes size attribute.

        Args:
            size (int): size of the square.

        Raises:
            TypeError: size must be an integer.
            ValueError: size must be >= 0.
        """
        self.__size = size
    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size
    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        """
        Calculates the area of square.

        Returns:
            int: Area of square.
        """
        return self.__size ** 2
