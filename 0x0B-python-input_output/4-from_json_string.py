#!/usr/bin/python3
"""Returns object from json string rep."""
import json


def from_json_string(my_str):
    """Returns object from json string representation.

    Args:
        my_str: The string.

    Returns:
        str: The string.
    """
    return json.loads(my_str)
