#!/usr/bin/python3
"""Creates a python object from a json string"""
def load_from_json_file(filename):
    """
    Creates a python object from a json file.

    Args:
        filename: the file to load json string from.

    Returns:
        python object
    """
    import json
    with open(filename, 'r') as file:
        python_object = json.load(file)
        return python_object
