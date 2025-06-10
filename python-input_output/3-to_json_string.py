#!/usr/bin/python3
import json
"""a function that returns the JSON representation of an object (string):"""


def to_json_string(my_obj):
    """
    returns JSON representation of an object

    Args:
        my_obj (void): the object used
    Returns:
        string
    """
    return json.loads(str(my_obj))
