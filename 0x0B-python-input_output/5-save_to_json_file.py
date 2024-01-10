#!/usr/bin/python3
""" writes an Object to a text file, using a JSON representation"""
def save_to_json_file(my_obj, filename):


    """
    this method saves a json representation to a file.

    Args:
        my_obj: python object source.
        filename: name of file to write json repre4sentation to

    Returns:
        none
    """
    import json
    with open(filename, 'w') as file:
        filename = json.dump(my_obj, file)
