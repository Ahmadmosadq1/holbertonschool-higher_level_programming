#!/usr/bin/python3
"""
This module prints the first name and last name in string
"""


def say_my_name(first_name, last_name=""):
    """ The function takes 2 arguments.

        Args:
        first_name: User's first name
        last_name: user's last name

    Returns:
        None

    Raises:
        TypeError: If either `first_name` or `last_name` is not a string.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
