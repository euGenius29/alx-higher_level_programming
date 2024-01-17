#!/usr/bin/python3
""" A derived class Rectangle with inheritance from Base"""

from models.base import Base

class Rectangle(Base):
    """ Models a rectangle object"""

    def __init__(self, width, height, x=0, y=0, id=None)-> None:
        """
        Instantiation of rectangle object

        Args:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
        x (int): the x value (defaults to 0).
        y (int): the y value (defaults to 0).
        id (int): id of object assigned from Base(defaults to None).
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self) -> int:
        """
        Returns the width

        Returns:
        int : width of the rectangle.
        """
        return(self.__width)


    @width.setter
    def width(self, value) -> int:
        """
        Setter method for width

        Args:
        value (int): value for the width
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @property
    def height(self) -> int:
        """
        Returns the height

        Returns:
        self.__height (int): value for the height.
        """
        return(self.__height)

    @height.setter
    def height(self, value) -> int:
        """
        Height setter method

        Args:
        value (int): value for height

        Raises:
        TypeError: if value is not an integer.
        ValueError: if value is 0 or less.
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
           raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self) -> int:
        """
        Returns value  of x

        Returns:
        self.__x (int): the int value of x
        """
        return(self.__x)

    @x.setter
    def x(self, value) -> int:
        """
        Setter method for x

        Args:
        value (int): int value for x

        Raises:
        TypeError: if value is not an integer.
        ValueError: if value is 0 or less.
        """
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value


    @property
    def y(self) -> int:
        """
        Returns the value of y

        Returns:
        self.__y (int): value for y
        """
        return(self.__y)

    @y.setter
    def y(self, value) -> None:
        """
        Setter method for y.

        Args:
        value (int): value for x

        Raises:
        TypeError: if value is not an integer.
        ValueError: if value is 0 or less.
        """
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self) -> None:
        """
        Calculates the area of the rectangle.

        Returns: area of the rectangle.
        """
        return (self.__width * self.__height)

    def display(self) -> None:
        """
        Displays the area using '#'

        """
        for j in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(' ', end='')
            for i in range(self.__width):
                print('#', end='')
            print()


    def __str__(self):
        """
        A method to customise __str__.

        Returns:
        (str) : customised in a specified way.
        """
        return (f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")


    def update(self, *args , **kwargs):
        """
        Updates the rectangle attributes using positional arguments.
        """
         
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)


    def to_dictionary(self) -> dict:
        """
        Returns the dictionary representation of a rectangle.
        
        Returns:
        (dict): dict rep of the rectangle.
        """
        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}

