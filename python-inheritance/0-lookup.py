#!/usr/bin/python3
"""A function returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Fucntion takes an object and extract its attributes and methods

    Arguments (obj):
            the Object.

    raises:
            None

    return:
            A list object
    """
    return dir(obj)
