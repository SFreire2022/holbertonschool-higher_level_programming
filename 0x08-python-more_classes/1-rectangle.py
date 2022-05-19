#!/usr/bin/python3
"""Module Rectangle"""


class Rectangle:
    """Definition for class Rectangle adding
    first atributes width and height"""
    def __init__(self, width=0, height=(0, 0)):
        self.size = size
        self.position = position

    @property
    def width(self):
        """Method to define attribute width to use with setter."""
        return self.__width

    @size.setter
    def width(self, new_width):
        """Method to set the private attribute width."""
        if not isinstance(new_width, int):
            raise TypeError("width must be an integer")
        if new_width < 0:
            raise ValueError("width must be >= 0")
        self.__width = new_width

    @property
    def height(self):
        """Method to define attribute height to use with setter."""
        return self.__size

    @size.setter
    def height(self, new_height):
        """Method to set the private attribute height."""
        if not isinstance(new_height, int):
            raise TypeError("height must be an integer")
        if new_height < 0:
            raise ValueError("height must be >= 0")
        self.__height = new_height
