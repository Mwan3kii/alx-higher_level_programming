#!/usr/bin/python3
'''Module for Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This defines subclass square."""

    def __init__(self, size):
        """defines size of rectangle.

        Args:
            size: The size of rectangle.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    def area(self):
        """Returns area.

        Returns:
            area: The area
        """
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation."""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
