#!/usr/bin/python3
"""A moudle that can both serilize objects to JSON and deserilize it back
to python object"""


import json


def serialize_and_save_to_file(data, filename):
    """selizeing the filename containing the data
    Args:
        data (str): the data in the file
        filename(str): the filename
    returns:
        int: number of charachters written in the file
    """
    my_seriliazed_data = json.dumps(data)
    """turning data to json fromat and then creating a file
    to write json data formatted into it"""

    with open(filename, 'w') as f:
        return f.write(my_seriliazed_data)


def load_and_deserialize(filename):
    """opening file in a read mode and load it using json.load"""
    """i only do f.read() if i want to load json as a string"""
    with open(filename, 'r') as f:
        return json.load(f)
