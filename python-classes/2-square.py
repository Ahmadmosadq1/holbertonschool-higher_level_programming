#!/usr/bin/python3
""" A class that defines a square
- The size has to be an integer and larger than 0"""


class Square:
    """This class has one private attribute which is size

    Attributes:
        size (int): Represents the size of the square.
    """
    def __init__(self, size=0):
        """
        This is an intance initiolizer
        It also contains the


        Arguement:
        Size: the square size which is a private class instance.
    """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
