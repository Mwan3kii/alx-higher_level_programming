#!/usr/bin/python3
"""This is a class Square that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits attributes from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes attributes of rectangle.

        Args:
            size: Value to assign to width and height.
            x: Cordinate.
            y: Cordinate.
            id: Unique identifiction.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns String representation method of square."""
        return "[Square] ({}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.size
        )

    @property
    def size(self):
        """Gets the size."""
        return self.width

    @size.setter
    def size(self, size):
        """Sets the value of size."""
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = size
            self.height = size

    def update(self, *args, **kwargs):
        """Assigns args to attributes usinf args and kwargs."""
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for p in range(len(args)):
                setattr(self, attributes[p], args[p])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of a square."""
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y,
        }
