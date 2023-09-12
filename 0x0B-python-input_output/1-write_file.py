#!/usr/bin/python3
"""This module writes a string to a text file"""


def write_file(filename="", text=""):
    """
        This function writes a string to a text file (UTF8) and returns the number of characters written:
    """
    with open(filename, encoding='utf-8', mode='w') as my_file:
        return my_file.write(text)
