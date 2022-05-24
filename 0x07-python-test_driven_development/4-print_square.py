#!/usr/bin/python3
"""
Module 4-print_square that prints a square with the character #.

Prototype: def print_square(size):
size is the size length of the square
size must be an integer, otherwise raise a
TypeError exception with the message size must be an integer
if size is less than 0, raise a
ValueError exception with the message size must be >= 0
"""


def print_square(size):
    """
    prints a square with the character #
    size is the size length of the square
    size must be an integer
    size must be greater than zero
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print('#' * size)
