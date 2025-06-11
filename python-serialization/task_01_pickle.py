#!/usr/bin/python3
"""a moudle to  serialize and deserialize custom Python objects
using the pickle module"""


import pickle


class CustomObject:
    """creating a custom claas"""
    def __init__(self, name, age, is_student):
        """initiolazing the objects"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        looping throigh the object created (self) by iterating its
        keys and values of the dunder method __dict__"""
        for key, val in self.__dict__.items():
            print("{}: {}".format(key, val))

    def serialize(self, filename):
        """
        This method will take a filename as its parameter.
        Using the pickle module, it will serialize the current instance
        """
        with open(filename, 'wb') as f:
            """opening a file in a write binary mode"""
            pickle.dump(self, f)

        @classmethod
        def deserialize(cls, filename):
            """opening a file with read binary mode"""
            try:
                with open(filename, 'rb') as f:
                    return pickle.load(f)
            except(FileNotFoundError, pickle.UnpicklingError):
                return None
