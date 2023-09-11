#!/usr/bin/python3
"""
    This returns the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """This function looks out --- all attributes and methods of an object"""
    return list(dir(obj))
