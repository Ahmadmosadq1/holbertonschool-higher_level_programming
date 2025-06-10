#!/usr/bin/python3
"""A function that reads a file"""


def read_file(filename=""):
    """
    Reads a file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, 'r') as f:
        """opeining a file in a read mode"""
        print(f.read())
