#!/usr/bin/python3
"""This writes an object to text file."""
import json


def save_to_json_file(my_obj, filename):
    """This writes oject file using json representation.

    Args:
        my_obj: The object.
        filename: Th filename.
    """
    with open(filename, 'w', encoding='utf=8') as file:
        content = json.dumps(my_obj)
        file.write(content)
