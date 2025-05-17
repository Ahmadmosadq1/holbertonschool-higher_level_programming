#!/usr/bin/python3
"""
This module does the addition operation of arguments a and b
The funcion also converts a float to an integr
"""


def add_integer(a, b=98):
    """ Addition function that takes 2 arguments and adds them.

    Args:
        a: First number (integer or float)
        b: Second number (integer or float)

    Returns:
        int: the sum of the two arguments

    Raises:
        if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):  # checks the type
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    try:
        return int(a) + int(b)
    except OverflowError:
        raise OverflowError("float overflow")
