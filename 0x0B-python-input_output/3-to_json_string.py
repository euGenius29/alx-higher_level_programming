#!/usr/bin/python3
"""
writes serializes a string as JSON file
"""
def to_json_string(my_obj):


    """
    serialises a python object as a JSON file

    Args:
        my_obj: the python object to serialize

    Returns:
        The serialized JSON sring
    """
    import json
    return (json.dumps(my_obj))
