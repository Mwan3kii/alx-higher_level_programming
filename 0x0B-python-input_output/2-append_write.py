#!/usr/bin/python3
"""This appends a string at file."""


def append_write(filename="", text=""):
    """Appends a string.

    Args:
        filename: The file name.
        text: The text.

    Returns:
        str: The number of characters.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
