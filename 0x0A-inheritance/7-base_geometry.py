#!/usr/bin/python3
"""Module containing Class definition for BaseGeometry"""


class BaseGeometry():
    """Constructor of the class"""

    def area(self):
        """Method to calculate area, not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate if value is an integer, name is alwas a string"""
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')
