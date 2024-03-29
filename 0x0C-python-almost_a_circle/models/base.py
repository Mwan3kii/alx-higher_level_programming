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
        if self.id < 0:
            raise ValueError("id must be >= 0")

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
            list_objs: The list of objects.

        Returns:
            Written json string to a file.
        """
        if list_objs is None:
            list_objs = []
        list_objs = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_objs)
        cls_name = cls.__name__
        filename = "{}.json".format(cls_name)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Converts json string rep to list using loads."""
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creating a dummy instance."""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy_instance = Rectangle(1, 1)
        elif cls is Square:
            dummy_instance = Square(1)
        else:
            dummy_instance = None
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns list of intances from a json file."""
        from os import path
        cls_name = cls.__name__
        file = "{}.json".format(cls_name)
        if not path.isfile(file):
            return []
        with open(file, 'r', encoding="utf-8") as f:
            json_string = f.read()
            return [
                    cls.create(**d)
                    for d in cls.from_json_string(json_string)
            ]

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
        """Draws the rectangles and squares."""
        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.title("Draw Rectangles and Squares")

        for rectangle in list_rectangles:
            Base.draw_shape(rectangle)
        for square in list_squares:
            Base.draw_shape(square)
        turtle.done()

    @staticmethod
    def draw_shape(shape):
        """Draws shape using Turtle."""
        turtle.penup()
        turtle.goto(shape.x, shape.y)
        turtle.pendown()
        turtle.color("black")
        turtle.begin_fill()

        for _ in range(5):
            turtle.forward(shape.width)
            turtle.left(90)
        turtle.end_fill()
        turtle.penup()
