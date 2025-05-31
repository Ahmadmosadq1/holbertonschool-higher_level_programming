#!/usr/bin/python3
"""ceating BaseGeometry class"""


class BaseGeometry:
    """ A class with no methods only Pass"""
    def area(self):
        """a method raises an exception error if called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """height and width validation: the number must be integer and > 0"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Creating a class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """creating init method to create intances"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
print(issubclass(Rectangle, BaseGeometry))