#!/usr/bin/python3
"""This ---- writes a string to a text file"""


def write_file(filename="", text=""):
    """
        This function writes a string to a text file and returns the number -- characters written:
    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        return my_file.write(text)
