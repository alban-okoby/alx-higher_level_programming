#!/usr/bin/python3

"""A magic method"""
def magic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return "BestSchool" + (", BestSchool" * (magic_string.n - 1))
