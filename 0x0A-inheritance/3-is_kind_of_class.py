#!/usr/bin/python3
"""Module containing a function to detect if an object is an instans of a
class inherited from the specified class"""


def is_kind_of_class(obj, a_class):
    """Function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False"""
    return isinstance(obj, a_class)
