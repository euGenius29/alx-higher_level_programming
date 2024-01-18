#!/usr/bin/python3
""" A base class. """

import json
import csv
import os


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

    @staticmethod
    def to_json_string(list_dictionaries) -> str:
        """
        Converts a dictionary to json string.

        Args:
         list_dictionaries (dict): dictionary to convert to json string.

        Returns:
        json_string (str): json string representation of dict.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '"[]"'

        elif type(list_dictionaries) is not list:
            raise TypeError("not a list of dictionaries")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs: list) -> None:
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

    @staticmethod
    def from_json_string(json_string: str) -> list:
        """
        Returns a python dictionary from a JSON string.

        Args:
        json_string (str): json string to convert to python dictionary.

        Returns:
        python dictionary object.
        """
        if json_string is None or len(json_string) == 0:
            return[]
        else:
            return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary: dict):
        """
        Returns an instance with all attributes already set

        Args:
        dictionary (dict): reference to instance

        Returns:
        instance with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        A method to return a list of instances

        Agrs:
        cls: class name

        Returns:
        a list of instances
        """
        try:
            with open(f"{cls.__name__}.json", "r") as file:
                result = file.read()
                result = cls.from_json_string(result)
                return [cls.create(**obj) for obj in result]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        A method to save a list of dictionaries to csv file.

        Args:
        cls: class name
        list_objs (list): list of dictionaries.
        """
        with open(f"{cls.__name__}.csv", "w") as csvfile:

            if list_objs is None or len(list_objs) == 0:
                csvfile.write("[]")
                return

            if cls.__name__ == 'Rectangle':
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == 'Square':
                fieldnames = ['id', 'size', 'x', 'y']

            else:
                raise ValueError(f" Unsupported class: {cls.__name__}")

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        data = []
        try:
            if os.path.exists(filename):
                with open(filename, 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        #for key in ["width", "height", "size", "x", "y"]:
                        for key in row:
                            row[key] = int(row[key])
                        data.append(row)
                return [cls.create(**obj) for obj in data]
        except FileNotFoundError:
            return[]
