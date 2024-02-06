#!/usr/bin/python3
"""Returns json string represention."""
import json


def to_json_string(my_obj):
    """Returns json string rep of object.

    Returns:
        str: Json string.
    """
    return json.dumps(my_obj)
