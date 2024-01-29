#!/usr/bin/python3
"""This is a class Rectangle."""


class Rectangle:
    """This is a class Rectangle.

    Attributes:
            width: The width of rectagle.
            height: The height os rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes width and height.

        Args:
            width: The width of rectagle.
            height: The height os rectangle.

        Raises:
            TypeError: width must be an integer.
            ValueError: width must be >= 0.
        """
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """Gets the width.

        Returns:
            width: the width.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the width.

        Args:
            value (int): the value to set to.

        Raises:
            TypeError: width must be an integer.
            ValueError: width must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """Gets the height of it.

        Returns:
            height: the height of rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the height of the rectagle.

        Args:
            Value (int): the value to be set.

        Raises:
            TypeError: width must be an integer.
            ValueError: width must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = value
