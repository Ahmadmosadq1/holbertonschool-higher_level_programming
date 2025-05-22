#!/usr/bin/python3
""" A class that finds the area of a square"""


class Square:
    """
    This class has one private attribute which is size

    Attributes:
        size (int): Represents the size of the square.
    """
    def __init__(self, size=0):
        """
        This is an intance initiolizer

        Arguement:
        Size: the square size which is a private class instance.
        """
        self.size = size

    @property
    def size(self):
        """
        this function is used as a getter for the private inactance size
        It is not a method anymore. it is a property
        """
        return self.__size

    @size.setter
    def size(self, size_value):
        """
        Here, we set and validate our
        """
        if not isinstance(size_value, int):
            raise TypeError("size must be an integer")
        if size_value < 0:
            raise ValueError("size must be >= 0")
        self.__size = size_value

    def area(self):
        """
        This function returns the area of the square
        """
        return self.__size * self.__size
