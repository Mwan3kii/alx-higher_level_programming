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

    def to_json(self, attrs=None):
        """Retrives dictiionary representation.

        Args:
            attrs: list of strings.

        Returns:
            The serialized data.
        """
        d_attrs = ["first_name", "last_name", "age"]
        if attrs is not None and isinstance(attrs, list):
            serialized = {attr: getattr(self, attr, None) for attr in attrs}
        else:
            serialized = {attr: getattr(self, attr, None) for attr in d_attrs}
        return serialized

    def reload_from_json(self, json):
        """This replaces all atributes os student.

        Args:
            json_data: The data.
        """
        for key, value in json.items():
            setattr(self, key, value)
