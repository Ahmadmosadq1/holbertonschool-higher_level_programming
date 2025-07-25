#!/usr/bin/python3
"""A function that writes a file"""


def write_file(filename="", text=""):
    """
    writes a file with a text content.

    Args:
        filename (str): The name of the file to read.
        text (str): the content of the file to be writtent

    Returns:
        f.write()
    """
    with open(filename, 'w') as f:
        """opeining a file in a write mode"""
        return f.write(text)
