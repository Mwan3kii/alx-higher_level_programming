#!/usr/bin/python3
'''Module for Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This does area of rectangele."""

    def __init__(self, size):
        """Does area of square.
        Args:
            size: The size.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Does area.

        Returns:
            area: The area.
        """
        return self.__size ** 2
