#!/usr/bin/python3
"""
This library is very simple, since it only has one function called
``add_integer()``.
Prototype: ``def add_integer(a, b=98):``
* a and b must be integers or floats, otherwise raise a
TypeError exception with the message:
``a must be an integer or b must be an integer``
* a and b must be first casted to integers if they are float.
* Return integer addition.
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
