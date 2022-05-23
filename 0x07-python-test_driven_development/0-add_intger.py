#!/usr/bin/python3
"""
0-add_integer.py module
Containing just one function
Prototype add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """ Adds two integers
    a and b should be int or float type
    otherwise raise TypeError Exception
    for first wrong type arg.
    Cast float to int before addition
    return int addition"""

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
