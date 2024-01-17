#!/usr/bin/python3
""" A base class. """

import json

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


    def to_json_string(list_dictionaries) -> dict:
        """
        Converts a dictionary to json string.

        Args:
         list_dictionaries (dict): dictionary to convert to json string.

        Returns:
        json_string (str): json string representation of dict.
        """
        if not list_dictionaries:
            return '"[]"'
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs) -> None:
        """
        Saves the json string to file

        Args:
        list_objs: list objects
        """
        if list_objs is None or len(list_objs) == 0:
            with open(f"{cls.__name__}.json", 'w') as file:
                file.write('[]')
                return
        else:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
            with open(f"{cls.__name__}.json", 'w') as file:
                file.write(cls.to_json_string(list_dictionaries))
