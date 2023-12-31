#!/usr/bin/python3
""" A class that defines a squre by size and raises exceptions
"""


class Square:
    """
    This is the Square class.

    Attributes:
    - __size (int): Private instance attribute repping the size of the square.

    Methods:
    - __init__(self, size=0): Initializes a new instance of the Square class.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class with an optional size.

        Args:
        - size (int, optional): The size of the square. Defaults to 0.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self)
    """
        Computes and returns the current square area.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2
