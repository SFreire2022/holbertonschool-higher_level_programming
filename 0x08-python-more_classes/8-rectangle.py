#!/usr/bin/python3
"""Module Rectangle"""


class Rectangle:
    """Definition for class Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Return representation string to print rectangle with #
        by default or any given symbol"""
        if self.width == 0 or self.height == 0:
            return ''
        my_string = ''
        for x in range(self.height):
            for y in range(self.width):
                my_string += str(self.print_symbol)
            if x != self.height - 1:
                my_string += '\n'
        return my_string

    def __repr__(self):
        """Method that return a string representation of the rectangle
        to be able to recreate a new instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Method executed when an object is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """Static method that returns the biggest rectangle
        based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
