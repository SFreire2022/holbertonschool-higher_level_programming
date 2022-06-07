#!/usr/bin/python3
""" Module containing just one class definition for Square
that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Model definition that inherits from Rectangle
    Private class atributes """

    def __init__(self, size, x=0, y=0, id=None):
        """ Public class instance constructor, initialize atributes and
        Call Super Class Constructor with super().__init__() """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Method to define attribute size to use with setter and
        asign to the super class atribute width. """
        return self.width

    @size.setter
    def size(self, new_size):
        """ Method to set the private attributes width and height to
        the same value size. """
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        if new_size <= 0:
            raise ValueError("size must be > 0")
        self.width = new_size
        self.height = new_size

    def __str__(self):
        """ Method to return [Square] (<id>) <x>/<y> - <size> """
        outputstr = '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.size)
        return outputstr

    def update(self, *args, **kwargs):
        """ Method to update attributes using args and kwargs """
        correct_args = ['id', 'size', 'x', 'y']
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
