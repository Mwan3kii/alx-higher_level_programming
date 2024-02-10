#!/usr/bin/python3
"""Creates class Base with private attribute."""


class Base:
    """Defines private attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes public instance id.

        Args:
            id (int): Unique identifier of each instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
