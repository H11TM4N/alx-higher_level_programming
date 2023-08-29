#!/usr/bin/python3
"""A class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """A Square"""

    def __init__(self, size=0):
        """Initialization of a new square

    Args:
        size (int): The first parameter.

    Returns:
        None
    """
        self.__size = size
        try:
            size >= 0
        except (ValueError, TypeError):
            print("Error")
