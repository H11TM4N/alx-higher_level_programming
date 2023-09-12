#!/usr/bin/python3
"""This module writes a string to a text file"""


def write_file(filename="", text=""):
    """
        This function writes a string to a text file (UTF8) and returns the number of characters written:
    """
    with open(filename, mode='w' encoding='utf-8') as my_file:
        print(my_file.write(text))
