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
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the rectangle’s width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle’s width, requiring an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the rectangle’s height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle’s height, requiring an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method returns the area of the rectangular"""
        return self.__width * self.__height

    def perimeter(self):
        """Method returns the perimeter of the rectangler"""
        if self.height == 0 or self.width == 0:
            """If height or weight is zero, the perimeter returns 0"""
            return 0
        return 2 * (self.height + self.__width)

    def __str__(self):
        """Method to print rectangualr starts"""

        """retuns an empty string if either is zero"""
        if self.height == 0 or self.width == 0:
            return ""
        """ multipling width by # in a row and looping through all loops
        in an (N)height
        """
        return "\n".join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        """ function returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)
