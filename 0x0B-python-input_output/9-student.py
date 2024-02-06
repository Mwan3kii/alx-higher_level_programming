#!/usr/bin/python3
"""This defines a class student."""


class Student:
    """Defines public instance attributes."""
    def __init__(self, first_name, last_name, age):
        """Initializes intances.

        Args:
            first_name: The filename
            last_name: The last name.
            age: The age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrives dictiionary representation.

        Returns:
            The serialized data.
        """
        serialized_data = {}
        for attr in ["first_name", "last_name", "age"]:
            value = getattr(self, attr)
            if isinstance(value, (str, int, bool)):
                serialized_data[attr] = value
        return serialized_data
