#!/usr/bin/python3
"""This is a function that prints with delimeters.
"""


def text_indentation(text):
    """Prints with delimeters.

    Args:
        text (str): The text in string.

    Raises:
        TypeError: text must be a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in ".?:":
        text = (delim + "\n\n").join([line.strip(" ") for line in text.split(delim)])
    print(text, end="")

