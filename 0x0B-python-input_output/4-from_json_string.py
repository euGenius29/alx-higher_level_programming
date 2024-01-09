#!/usr/bin/python3
""" Converts JSON string to python object"""
def from_json_string(my_str):
    """
    Returns a python object from a JSON string.

    Args:
    my_str: json string to create python object from

    Returns:
    python object.
    """
    import json
    return(json.loads(my_str))
