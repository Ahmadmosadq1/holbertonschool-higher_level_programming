#!/usr/bin/python3
""" Creating an empty class named rectangler
it only passes
"""


class Rectangle:
    """
    a class only passes with no methods

    Attributes:
        attr (str): No attributes.

    """
    def __init__(self, width=0, height=0):
        """Initialize the instance with the given width and height."""
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """Return the rectangle’s width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle’s width, requiring an int >= 0."""
        if isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """Return the rectangle’s height."""
        return self.__height

    @width.setter
    def width(self, value):
        """Set the rectangle’s height, requiring an int >= 0."""
        if isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


    
