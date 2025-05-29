#!/usr/bin/python3
""" A function that returns True only if the object is not direct intance
of its direct class
"""


def is_kind_of_class(obj, a_class):

    """function takes two arguments . obj and a_class

    Arguments:
            Obj: an instance of a class
            a_class: the object
    raise:
            Not

    return:
            True or False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
