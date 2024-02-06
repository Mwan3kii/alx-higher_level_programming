#!/usr/bin/python3
"""This reads a file."""


def read_file(filename=""):
    """Reads a file and prints in stdout.

    Args:
        filename: The name of file.
    """
    with open("my_file_0.txt", 'r') as file:
        content = file.read()
    print(content, end="")
