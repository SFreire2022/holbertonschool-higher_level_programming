#!/usr/bin/python3
"""Module containing Class definition for Rectangle class
inherited from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Constructor of the Class Rectangle"""

    def __init__(self, width, height):
        """Initialization of width and height private atribs"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Method to return the area calculation"""
        return(self.__width * self.__height)

    def __str__(self):
        """str will executes when print method is used"""
        return (f'[Rectangle] {self.__width}/{self.__height}')
