#!/usr/bin/python3
"""This defines area in class."""


class BaseGeometry():
    """Defines an area but not implemented."""

    def area(self):
        """Defines an area in class.

        Raises:
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Defines a public intance method.

        Args:
            name (str): The name.
            value (int): The value to use.

        Raises:
            TypeError: must be integer.
            ValueError: must be greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
class Rectangle(BaseGeometry):
    """This inherits from basegeometry."""

    def __init__(self, width, height):
        """This sets and validates width and heights.

        Args:
            width: The width of rectangle.
            height: The height of rectangle.
        """
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
