#!/usr/bin/python3
"""Creates object from json file."""
import json


def load_from_json_file(filename):
    """Creates object from json file.

    Args:
        filename: The filename.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        json_content = file.read()
        return json.loads(json_content)
