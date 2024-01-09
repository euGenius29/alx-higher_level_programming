#!/usr/bin/python3
""" Script writes a file and returns the number of characters written."""

def write_file(filename="", text=""):
    """
    A method to write text to a file and return the number of characters printed

    Args:
       filename: name of file to create/overwrite
       text: the text content to place in file.

    Returns:
       The number of characters appended
            
    """

    with open(filename, 'w') as file:
        file.write(text)

    return len(text)
