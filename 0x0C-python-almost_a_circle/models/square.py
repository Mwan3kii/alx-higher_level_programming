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
                self.id, self.x, self.y, self.width
        )
