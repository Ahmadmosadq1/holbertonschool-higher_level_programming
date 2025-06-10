#!/usr/bin/python3
"""creating a function for Json serilization"""


def class_to_json(obj):
    """derseriliazing the object intance"""
    return obj.__dict__
