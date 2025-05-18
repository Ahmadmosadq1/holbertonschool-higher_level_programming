#!/usr/bin/python3
"""
This function creates square shapes with #
It must be an int and bigger than or equale to zero
"""


def print_square(size):
    """ Fucntion takses one size argument and prints # in squares.

        Args:
        Size: the size of the square

    Returns:
        None

    Raises:
        "TypeError": if a size is not int or float lesst than zero,
        it will trigger this erros

        "ValueError": triggered when the size < 0

    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for colm in range(size):
            print("#", end="")
        print()
