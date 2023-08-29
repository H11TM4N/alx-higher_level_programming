#!/usr/bin/python3
"""A class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """A Square"""

    def __init__(self, size=0):
        """Initialization of a new square

    Args:
        size (int): The first parameter.

    Returns:
        None
    """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
