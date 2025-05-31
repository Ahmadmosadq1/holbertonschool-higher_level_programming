#!/usr/bin/python3
"""importing modules from abc"""
from abc import ABCMeta, abstractmethod
"""Creating an abtracion class for Animal"""


class Animal(metaclass=ABCMeta):
    """An abtracted method for sound"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Dog class inherts from Animal"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class inherts from Animal"""
    def sound(self):
        return "Meow"
