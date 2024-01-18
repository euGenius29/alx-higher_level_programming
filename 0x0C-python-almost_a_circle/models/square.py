#!/usr/bin/python3
"""A class that models a square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Models a square object"""
    def __init__(self, size, x=0, y=0, id=None) -> None:
        """
        Instantiation of a square object

        Args:
        size (int): size of the square.
        x (int):the x value. defaults to 0.
        y (int): the y value. defaults to 0.
        id: the id of the object. defaults to None.
        """

        super().__init__(size, size, x, y, id)
        self.size = self.width

    @property
    def size(self) -> int:
        """
        Returns the size of the square instance

        Returns:
        size (int): the size of the square.
        """
        return (self.width)

    @size.setter
    def size(self, value) -> None:
        """
        setter method for size of the square.
        """
        self.width = value
        self.height = value

    def __str__(self) -> str:
        """
        customizes __str__ message
        """
        return (f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.size}")

    def update(self, *args, **kwargs) -> None:
        """
        Updates the square with new arguments
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self) -> dict:
        """
        Stores arguments of square to a dictionary

        Returns:
        (dict): dictionary representation of square's args
        """
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y,
                }
