#!/usr/bin/python3
"""creatign a class with serlization method"""


class Student:
    """class named student containg the first and last name and age"""
    def __init__(self, first_name, last_name, age):
        """initilaizing the intances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """preparing the data to be seriliazied laster using dumps"""
        return self.__dict__
