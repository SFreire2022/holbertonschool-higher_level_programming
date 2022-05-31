#!/usr/bin/python3
"""Module containing Class definition for Square class
inherited from Rectangle and BaseGeometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Constructor of the Class Square"""

    def __init__(self, size):
        """Initialization of size private atrib"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method to return the area calculation"""
        return(super().area())
