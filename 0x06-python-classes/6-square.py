#!/usr/bin/python3
"""
This is the Square module.

It defines a Square class with its attribtes
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
            size (int): The size of the square
            position (tuple): the position of size.

        Raises:
            TypeError: size must be an integer.
            ValueError: size must be >= 0
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Gets the size of the square.

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

    @property
    def position(self):
        """
        Get the position of square.

        Returns:
            tuple: position of square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets position of square

        Args:
            value (tuple): position to set.

        Raises:
            TypeError: position must be a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or \
                len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of the square.

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
            for _ in range(self.__position[1]):
                print()
            square_lines = [" " * self.__position[0] + "#" * self.__size for _ in range(self.__size)]
            print("\n".join(square_lines))
