#!/usr/bin/python3
"""a function that creates an Object from a “JSON file”"""

import json


def load_from_json_file(filename):
    """
    returns an object from JSON file

    Args:
        filename: the JSON file
    Returns:
        string
    """
    with open(filename, 'r') as my_file:
        return json.load(my_file)
