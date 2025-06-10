#!/usr/bin/python3
"""A function that appends to a file"""


def append_write(filename="", text=""):
    """
    appends to a file in each execution.

    Args:
        filename (str): The name of the file to read.
        text (str): the content of the file to be writtent

    Returns:
        f.append()
    """
    with open(filename, 'a') as f:
        """opeining a file in a append mode"""
        return f.write(text)
