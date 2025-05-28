#!/usr/bin/python3
""" A function that returns True if an instance belongs to a class
and False otherwise
"""


def is_kind_of_class(obj, a_class):

    """function takes two arguments . obj and a_class

    Arguments:
            Obj: an instance of a class
            class: the object
    raise:
            Not

    return:
            True or False
    """
    return isinstance(obj, a_class)
