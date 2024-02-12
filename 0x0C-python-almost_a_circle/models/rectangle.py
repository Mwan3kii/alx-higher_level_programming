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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__width = width

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        if type(value) != int:
            raise TypeError("{} must be an interger".format("width"))
        elif value <= 0:
            raise ValueError("{} must be > 0".format("width"))
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        if type(value) != int:
            raise TypeError("{} must be integer".format("height"))
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x."""
        if not isinstance(value, int):
            raise TypeError("x must be integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y."""
        if not isinstance(value, int):
            raise TypeError("y must be integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

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
