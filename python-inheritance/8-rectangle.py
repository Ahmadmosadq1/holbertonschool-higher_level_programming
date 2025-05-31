#!/usr/bin/python3
"""Module defining BaseGeometry and Rectangle classes."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raises an exception to indicate this is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer.

        Args:
            name (str): name of the value (for error messages)
            value (int): value to validate

        Raises:
            TypeError: if value is not an int
            ValueError: if value <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize width and height after validation."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
