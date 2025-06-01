#!/usr/bin/python3
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
    """
    Circle shape class.

    Parameters:
        radius (float): The radius of the circle.
    """
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
    """
    Rectangle shape class.

    Parameters:
        height (float): The height of the rectangle.
        width (float): The width of the rectangle.
    """
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


def shape_info(shape):
    """duck typing method"""
    print("Area:", shape.area())
    print("perimeter:", shape.perimeter())

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)