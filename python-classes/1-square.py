#!/usr/bin/python3
"""Creating a class that defines a square"""


class Square:
    """This class has one private attribute which is size

    Attributes:
        size (int): Represents the size of the square.
    """
    def __init__(self, size):
        """
        This is an intance initiolizer


        Arguement:
        Size: the square size
    """
        self.__size = size
