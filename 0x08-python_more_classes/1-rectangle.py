#!/usr/bin/python3
"""
A hashbang to invoke python3
"""

class Rectangle:
    """ A class that defines a rectangle with width and height attributes.
    Attributes:
    -width (int): width of the triangle.
    -height (int): height of the triangle.

    Methods:
    - width() -> int: Getter method for width.
    - width(value: int): Setter method for width.
    - height() -> int: Setter method for width.
    - width (value: int): Setter method for width.
    - __init__(width: int = 0, height: int = 0): Constructor wth width and height.
    """
    def __init__(self, width=0, height =0):
        """
        Initializes a rectangle instance.

        Args:
        - width (int): Width of the rectanlge (default is 0).
        - height (int): Height of the rectangle.
        """
        self.__width = width
        self.__height = height


    @property
    def width(self):
        """Getter method for width"""
        return self.__width


    def width(self, value):
        """
        Setter method for width.

        Args:
        - value (int): width value to set.

        Raises:
        - TypeError: If width is not an integer.
        - VaueError: If intger is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        """
        Getter method for width
        """
        return self.__height
    

    def height(self, value):
        """
        Setter method for height.

        Args:
        - value (int): height value to set.

        Raises:
        - TypeError: If height is not an integer.
        - VaueError: If intger is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
