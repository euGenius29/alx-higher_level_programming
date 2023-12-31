#!/usr/bin/python3
"""a class that defines a square by:(based on 2-square.py)"""


class Square:
    """ class of Square """
    def __init__(self, size=0):
        """Initialize the square with a given size """
        self.size = size

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

    def area(self):
        """Calculate and return the area of the square"""
        return self.__size ** 2
