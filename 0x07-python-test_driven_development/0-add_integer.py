#!/usr/bin/python3

""" An integer sum function"""


def add_integer(a, b=98):
    """Check if a and b are integers or can be casted to integers"""
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return (a + b)
