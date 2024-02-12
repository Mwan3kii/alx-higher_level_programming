#!/usr/bin/python3
"""Creates class Base with private attribute."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json string representation."""
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Calls a class method and writes json string to a file.

        Args:
            cls: Class to call.

        Returns:
            Written json string to a file.
        """
        if list_objs is None:
            return "[]"

        cls_name = cls.__name__
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)

        filename = "{}.json".format(cls_name)
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Converts json string rep to list using loads."""
        if json_string is None or json_string == "":
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creating a dummy instance."""
        dummy_instance = cls('width', 'height')
        dummy_instance.update(**dictionary)
        return dummy_instance
