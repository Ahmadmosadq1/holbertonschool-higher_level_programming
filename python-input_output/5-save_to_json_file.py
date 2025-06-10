#!/usr/bin/python3
"""a function that writes an Object to a text file, using a JSON
representation:"""

import json


def save_to_json_file(my_obj, filename):
    """
    returns an object from JSON to python object

    Args:
        my_obj (void): the object used
    Returns:
        string
    """
    with open(filename, 'w') as my_file:
        return json.dump(my_obj, my_file)
