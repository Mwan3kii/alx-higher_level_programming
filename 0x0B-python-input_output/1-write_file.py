#!/usr/bin/python3
"""This writes a string with with."""


def write_file(filename="", text=""):
    """This writes a string and returns number of character.

    Args:
        filename: The filename.
        text: The text to use.

    Returns:
        str: The number of character.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
