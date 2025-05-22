#!/usr/bin/python3
""" A class that finds the area of a square"""


class Square:
    """
    This class has one private attribute which is size

    Attributes:
        size (int): Represents the size of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        This is an intance initiolizer

        Arguement:
        Size: the square size which is a private class instance.
        position: its position
        """
        self.size = size
        self.position = position

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

    def my_print(self):
        """ This is a public inctance method for printing squares of #"""
        if self.__size == 0:
            print()
            return

        # vertical offset
        for _ in range(self.__position[1]):
            print()

            # each row: horizontal spaces then hashes
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """Retrieve the private position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Validate and set the private position."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value
