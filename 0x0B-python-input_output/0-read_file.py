#!/usr/bin/python3
"""This reads a file."""


def read_file(filename=""):
    """Reads a file and prints in stdout.

    Args:
        filename: The name of file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end="")
