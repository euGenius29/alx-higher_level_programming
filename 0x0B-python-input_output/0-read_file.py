#!/usr/bin/python3

""" A module that reads the contents of a file"""

def read_file(filename=""):
    """ 
    Reads the content of a file and prints it to stdout.

    Args:
        filename="": the file to open

    Returns:
        None

    Raises:
        None
    """
    
    with open(filename, 'r') as file:
        content = file.read()
        print(content, end ="")
