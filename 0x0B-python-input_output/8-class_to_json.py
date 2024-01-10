#!/usr/bin/python3

"""
A module that returns the dict description with data structures for JSON serialization"""


def class_to_json(obj: object) -> dict:
    """
    Returns the dictionary representation of a simple data structure for JSON serialization of an object..

    Args:
        obj (object): The object (a instance of a Class) to ready for
        JSON serialization.

    Returns:
        dict: The dictionary description of the object.
    """
    return (obj.__dict__)
