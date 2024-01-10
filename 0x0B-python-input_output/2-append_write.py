#!/usr/bin/python3
""" appends a string at the end and returns the number of chars"""

def append_write(filename="", text=""):


    """
    Divides all elements of a matrix.i

    Args:
        filename: name of the file.
        text: text to add to file.

    Returns:
        number of caracters added.

    """
    with open(filename, 'a') as file:
        file.write(text)

    return len(text)
