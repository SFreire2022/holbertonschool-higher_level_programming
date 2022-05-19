#!/usr/bin/python3
"""Module Rectangle"""


class Rectangle:
    """Definition for class Rectangle adding
    first atributes width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method to define attribute width to use with setter."""
        return self.__width

    @width.setter
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
        return self.__height

    @height.setter
    def height(self, new_height):
        """Method to set the private attribute height."""
        if not isinstance(new_height, int):
            raise TypeError("height must be an integer")
        if new_height < 0:
            raise ValueError("height must be >= 0")
        self.__height = new_height

    def area(self):
        """Method to calculate the area of Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Method to calculate the perimeter of Rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return representation string to print rectangle with #"""
        if self.width == 0 or self.height == 0:
            return ''
        my_string = ''
        for x in range(self.height):
            for y in range(self.width):
                my_string += '#'
            if x != self.height - 1:
                my_string += '\n'
        return my_string

    def __repr__(self):
        """Method that return a string representation of the rectangle
        to be able to recreate a new instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
