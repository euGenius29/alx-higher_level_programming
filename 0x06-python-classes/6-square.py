#!/usr/bin/python3
"""a class that defines a square by:(based on 5-square.py)"""


class Square:
    """ class of Square """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a given size """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            """set size to private if values can not print"""
            self.__size = value

    @property
    def position(self):
        """Getter method for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position"""
        if not isinstance(value, tuple) or len(value) != 2 or\
            not all(isinstance(i, int) for i in value) or not\
                all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate and return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#' and positioning."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
