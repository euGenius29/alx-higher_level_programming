#!/usr/bin/python3
""" A square class that defines a square by size
"""

class Square:
    """
    This is the Square class.

    Attributes:
    - __size (int): Private instance attributes repping size

    Methods:
    -None
    """
    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
        - size (int): The size of the square.
        """
        self.__size = size
