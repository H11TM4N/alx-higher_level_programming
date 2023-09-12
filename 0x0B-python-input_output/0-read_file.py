#!/usr/bin/python3
"""This module reads a text file"""


def read_file(filename=""):
    """
        This function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename) as my_file:
        print(my_file.read())
