#!/usr/bin/python3
"""This defines class Rectangle with subclass Base."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes private instance attributes.

        Args:
            id (int): Unique identifier for each instance
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle.
            y (int): Y-coordinate of the rectangle.
        """
        super().__init__(id)
        self.__validate_positive_int("width", width)
        self.__validate_positive_int("height", height)
        self.__validate_positive_int("x", x)
        self.__validate_positive_int("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__width = width

    def __validate_int(self, attribute, value):
        """Validate if a value is an integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attribute))

    def __validate_positive_int(self, attribute, value):
        """Validate if a value is a positive integer."""
        self.__validate_int(attribute, value)
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute))

    def __validate_greater_than(self, attribute, value):
        """Validates if width or height is less or equals to 0."""
        self.__validate_int(attribute, value)
        if value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter method for width."""
        self.__validate_greater_than("width", width)
        self.__width = width

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter method for height."""
        self.__validate_positive_int("height", height)
        self.__height = height

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter method for x."""
        self.__validate_positive_int("x", x)
        self.__x = x

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter method for y."""
        self.__validate_positive_int("y", y)
        self.__y = y

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Displays rectangle in # character."""
        for _ in range(self.y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """overriding the str method."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Sets arguments to attributes using args and kwargs."""
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of rectangle."""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y,
        }
