#!/usr/bin/python3
"""a function that returns an object (Python data structure)
represented by a JSON string"""

import json


def from_json_string(my_str):
    """
    returns an object from JSON to python object

    Args:
        my_obj (void): the object used
    Returns:
        string
    """
    return json.loads(my_str)
