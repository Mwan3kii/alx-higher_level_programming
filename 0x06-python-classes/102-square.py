#!/usr/bin/python3
"""This is a Square class."""


class Square:
    """This is a Square class.
    Attributes:
        __size (int, float): Size of square.
    """
    def __init__(self, size=0):
        """
        Initializes a private instance size.

        Args:
            size: The size of square.

        Raises:
            TypeError: Size must be integer.
            ValueError: Size must be >= 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrives the size of square
        Returns:
            float or int: Size of square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size.

        Args:
            value: The value of square.

        Raises:
            TypeError: Size must be integer.
            ValueError: Size must be >= 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of square.
        Returns:
            float or int: The area of square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparison based on the area of squares.

        Args:
        other (Square): Another square to compare.

        Returns:
        bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparison based on the area of squares.

        Args:
        other (Square): Another square to compare.

        Returns:
        bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than comparison based on the area of squares.

        Args:
            other (Square): Another square to compare.

        Returns:
            bool: True if the area is < the other area, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal to comparison based on the area of squares.

        Args:
            other (Square): Another square to compare.

        Returns:
            bool: True if the area is <= to the other area, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than comparison based on the area of squares.

        Args:
            other (Square): Another square to compare.

        Returns:
            bool: True if area is > other square's area, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal to comparison based on the area of squares.

        Args:
        other (Square): Another square to compare.

        Returns:
            bool: True if area is >= other area, False otherwise.
        """
        return self.area() >= other.area()
