#!/usr/bin/python3
"""This defines area in class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This inherits from basegeometry."""

    def __init__(self, width, height):
        """This sets and validates width and heights.

        Args:
            width: The width of rectangle.
            height: The height of rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
