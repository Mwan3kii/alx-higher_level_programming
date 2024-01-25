#!/usr/bin/python3
"""This is a magic class."""

import math


class MagicClass:
    """This is a magic class.

    Attributes:
        radius: the radius to be used.
    """
    def __init__(self, radius):
        """
        Initializes a radius instance.

        Args:
            radius: the radius.

        Raises:
            TypeError: radius must be a number.
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be an number")
        self.__radius = radius

    def area(self):
        """
        Does the area.

        Returns:
            Area: The area with the radius
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates circumfrence.

        Return:
            Circumfrence: With the radius.
        """
        return 2 * math.pi * self.__radius
