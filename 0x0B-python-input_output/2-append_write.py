#!/usr/bin/python3
""" appends a string at the end of a text file (UTF8) and returns the number of characters added"""

def append_write(filename="", text=""):
    """
    Divides all elements of a matrix.

    Args:
        filename: name of the file.
        text: text to add to file.

    Returns:
        number of caracters added.
    
    """
    with open(filename, 'a') as file:
        file.write(text)

    return len(text)
