#!/usr/bin/python3
"""Module Square"""


class Square:
    """Definition for class Square adding first atribute size and def value
	now adding possition attribute and default value"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
		self.position = position

    @property
    def size(self):
        """Getter Method to define attribute size to use with setter."""
        return self.__size

    @size.setter
    def size(self, new_size):
        """Method to set the private attribute size."""
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size

    @property
    def position(self):
        """Getter Method to define attribute position to use with setter."""
        return self.__position

    @position.setter
    def position(self, new_position):
        """Method to set the private attribute position"""
        if type(new_position) != tuple or len(new_position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(new_position[0]) != int or type(new_position[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if new_position[0] < 0 or new_position[1] < 0:
            raise ValueError('position must be a tuple of 2 positive integers')
        self.__position = new_position

    def area(self):
        """Public method to return the area"""
        return(self.__size * self.__size)

    def my_print(self):
        """Public method to print the square with the character #"""
        if self.size != 0:
            if self.position[1] is not 0:
                print('\n' * self.position[1], end='')
            for ch in range(self.size):
                print(' ' * self.position[0], end='')
                print('#' * self.size)
        else:
            print()
