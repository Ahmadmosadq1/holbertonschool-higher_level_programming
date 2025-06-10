#!/usr/bin/python3
"""creatign a class with pre-serlization method"""


class Student:
    """class named student containg the first and last name and age"""
    def __init__(self, first_name, last_name, age):
        """initilaizing the intances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dict of this instance’s attributes.

        If attrs is a list of strings, only include those keys
        (and only if they exist). Otherwise include everything.
        """
        if isinstance(attrs, list) and all (isinstance(a, str) for a in attrs):
            return{
                key:getattr(self, key)
                for key in attrs
                if hasattr(self, key)
            }
        else:
            return self.__dict__
