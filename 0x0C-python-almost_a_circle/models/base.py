#!/usr/bin/python3
"""Creates class Base with private attribute."""
import json
import csv
import turtle


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
        for key, value in dictionary.items():
            if key not in ["id"]:
                dictionary[key] = int(value)

        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns list of intances from a json file."""
        cls_name = cls.__name__
        filename = "{}.json".format(cls_name)
        if filename:
            with open(filename, 'r') as file:
                json_string = file.read()
                return [cls.create(**d) for d in cls.from_json_string(json_string)]
        else:
            return "[]"

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to csv."""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as file:
            if list_objs is not None:
                if cls.__name__ == 'Rectangle':
                    headers = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == 'Square':
                    headers = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Saves to csv."""
        filename = cls.__name__ + ".csv"
        if filename:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                return [cls.create(**row) for row in reader]
        else:
            return "[]"
    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.title("Draw Rectangles and Squares")

        pen = turtle.Turtle()
        pen.speed(2)

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.forward(rect.width)
            pen.right(90)
            pen.forward(rect.height)
            pen.right(90)
            pen.forward(rect.width)
            pen.right(90)
            pen.forward(rect.height)
            pen.right(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.forward(square.size)
            pen.right(90)
            pen.forward(square.size)
            pen.right(90)
            pen.forward(square.size)
            pen.right(90)
            pen.forward(square.size)
            pen.right(90)
        turtle.done()
