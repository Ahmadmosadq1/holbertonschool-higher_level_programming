#!/usr/bin/python3
"""ceating BaseGeometry class"""


class BaseGeometry:
    """ A class with no methods only Pass"""
    def area(self):
        """a method raises an exception error if called"""
        raise Exception("area() is not implemented")
