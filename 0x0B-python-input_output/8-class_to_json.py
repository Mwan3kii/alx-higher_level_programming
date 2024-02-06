#!/usr/bin/python3]
"""This returns dictionary description."""


def class_to_json(obj):
    """This returns dictionary desrition with simple data.

    Args:
        obj: The instance of class.

    Returns:
        The serialized attribute.
    """
    attr = obj.__dict__
    serialized_attr = {}
    for key, value in attr.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized_attr[key] = value
    return serialized_attr
