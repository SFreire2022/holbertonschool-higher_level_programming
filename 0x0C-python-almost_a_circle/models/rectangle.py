#!/usr/bin/python3
"""Module containing just one class definition for Rectangle
that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Class Model definition that inherits from base
    Private class atributes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Public class instance constructor, initialize atributes and
        Call Super Class Constructor with super().__init__"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Method to define attribute width to use with setter."""
        return self.__width

    @width.setter
    def width(self, new_width):
        """Method to set the private attribute width."""
        if not isinstance(new_width, int):
            raise TypeError("width must be an integer")
        if new_width <= 0:
            raise ValueError("width must be > 0")
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
        if new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height

    @property
    def x(self):
        """Method to define attribute x to use with setter."""
        return self.__x

    @x.setter
    def x(self, new_x):
        """Method to set the private attribute x."""
        if not isinstance(new_x, int):
            raise TypeError("x must be an integer")
        if new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    @property
    def y(self):
        """Method to define attribute y to use with setter."""
        return self.__y

    @y.setter
    def y(self, new_y):
        """Method to set the private attribute y."""
        if not isinstance(new_y, int):
            raise TypeError("y must be an integer")
        if new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

    def area(self):
        """ Public method to calculate the area for teh Rectangle instance """
        return (self.width * self.height)

    def display(self):
        """ Prints to stdout the Rectangle instance with the character # """
        for y in range(self.height):
            print("#" * self.width)
