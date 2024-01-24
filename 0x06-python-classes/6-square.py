#!/usr/bin/python3
"""
This is the Square module.

It defines a Square class with private size and position attributes,
size and position properties, area method, and my_print method.
"""


class Square:
    """
    This is square class.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or position contains negative integers.
        """
        self.__size = size
        self.__position = position
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
    def position(self):
        """
        Retrieves the position of square.

        Returns:
            tuple: position of square.
        """
        return self.__position
    def position(self, value):
        """
        Sets position of square

        Args:
            value (tuple): position to set.

        Raises:
            TypeError: position must be a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
            not all(isinstance(i, int) and i >= 0 for i in value):
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
    def my_print(self):
        """
        Prints the square using '#' characters.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for row in range(self.__position[1]):
                print()
            for row in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
