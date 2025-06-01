#!/usr/bin/python3
"""importing modules from abc"""
from abc import ABCMeta, abstractmethod
import math
"""creating an abstract class shape"""


class Shape(metaclass=ABCMeta):
    """the class has two abtracted methods. area and perimeter"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        """initilizing raduius"""
        self.radius = radius

    def area(self):
        """defining the area of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """defining the perimeter of the circle"""
        return self.radius * math.pi * 2


class Rectangle(Shape):
    def __init__(self, height, width):
        "initiolizing height and width "
        self.height = height
        self.width = width

    def area(self):
        """defining the area of the rectangular"""
        return self.height * self.width

        def perimeter(self):
            """perimeter the area of the rectangular"""
            return 2 * (self.height + self.width)
