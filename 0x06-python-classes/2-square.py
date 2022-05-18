#!/usr/bin/python3
"""Module Square"""


class Square:
    """Definition for class Square adding first atribute size and def value"""
    def __init__(self, size=0):
        """Private instance attribute: size
            -Check int data type, if not rise TypeError exception
			-Check if value is positive, if not rise ValueError exception"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
