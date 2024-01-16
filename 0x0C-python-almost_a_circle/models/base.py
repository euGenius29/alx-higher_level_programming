#!/usr/bin/python3
""" A base class. """

class Base:
    """
    A base class with private class attribute and constructor.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation of the Base object.

        Args:
        id (int, optional): ID of the object, defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
