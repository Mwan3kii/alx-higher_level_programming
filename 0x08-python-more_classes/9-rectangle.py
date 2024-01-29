#!/usr/bin/python3
"""This is a class Rectangle."""


class Rectangle:
    """This is a class Rectangle.

    Attributes:
            width: The width of rectagle.
            height: The height os rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width.

        Returns:
            width: The width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width.

        Args:
            value (int): The value to set to.

        Raises:
            TypeError: Width must be an integer.
            ValueError: Width must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of it.

        Returns:
            height: The height of rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectagle.

        Args:
            Value (int): The value to be set.

        Raises:
            TypeError: Height must be an integer.
            ValueError: Height must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        This calculates area of rectangle.

        Returns:
            int: The area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates perimeter of rectangle.
        Returns:
            int: The perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns str representation of the rectangle using #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for _ in range(self.__height):
            result += str(self.print_symbol) * self.__width + '\n'
        return result[:-1]

    def __repr__(self):
        """Returns a string rep of rectangle.

        Returns:
            str: A string representations of rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.

        Args:
            rect_1: First rectangle.
            rect_2: Second rectangle.

        Raises:
            TypeError: Must be an instanc of rectangle.

        Returns:
            Rectangle: That has bigger area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates new Rectangle instance.

        Args:
            size: Size of square.

        Returns:
            Rectangle: The new rectangle rep a square.
        """
        return cls(size, size)
