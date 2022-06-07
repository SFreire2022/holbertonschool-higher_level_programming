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
        """ Prints to stdout the Rectangle instance with the character #
        Now taking care of xy position """
        print("\n" * self.y, end="")
        for y in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """ Method to return [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        outputstr = '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height)
        return outputstr

    def update(self, *args, **kwargs):
        """ Method to update attributes using args and kwargs """
        correct_args = ['id', 'width', 'height', 'x', 'y']
        if len(args) > 0:
            if len(args) > len(correct_args):
                args_len = len(correct_args)
            else:
                args_len = len(args)
            for i in range(args_len):
                setattr(self, correct_args[i], args[i])
        elif kwargs is not None:
            for key in kwargs:
                if hasattr(self, key) is True:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Method that returns the dictionary representation of a Rectangle"""
        list_atrib = ['id', 'width', 'height', 'x', 'y']
        dict_rep = {}
        for key in list_atrib:
            dict_rep[key] = getattr(self, key)

        return dict_rep
