#!/usr/bin/python3
"""a class that defines a square by:(based on 2-square.py)"""


class Square:
    """ class of Square """
    def __init__(self, size=0):
        """Initialize the square with a given size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            """set size to private if values can not print"""
            self.__size = size

    def area(self):
        """Calculate and return the aread of the square"""
        return self.__size ** 2
