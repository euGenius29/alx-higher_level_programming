#!/usr/bin/python3

"""
A script that adds all arguments to a python list and save them to a JSON file
"""

import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_to_json_file(args, json_file: str = "add_item.json"):
    """adds all cmd line args to a python list, and serializes to a json file

    Args:
        args: command line arguments
        json_file (str): The name of JSON file to write to.

    """
    py_list = []

    try:
        py_list = load_from_json_file(json_file)
    except Exception:
        save_to_json_file([], json_file)

    for arg in args:
        py_list.append(arg)

    save_to_json_file(py_list, json_file)


if __name__ == "__main__":
    add_to_json_file(sys.argv[1:])
