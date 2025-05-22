#!/usr/bin/python3
""" A class that finds the area of a square"""


class Square:
    """This class has one private attribute which is size

    Attributes:
        size (int): Represents the size of the square.
    """
    def __init__(self, size=0):
        """
        This is an intance initiolizer

        Arguement:
        Size: the square size which is a private class instance.
    """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ This is a public instance method for finding an area of a square"""
        return self.__size * self.__size
