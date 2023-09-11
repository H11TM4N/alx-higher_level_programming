#!/usr/bin/python3
"""
    This funcion verifies an object class
"""


def is_kind_of_class(obj, a_class):
    """
    Verify if an object is an instance of, or inherited from, the specified class.

    Args:
        obj (object): The object to be checked.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass; otherwise, False.
    """
    return isinstance(obj, a_class)
