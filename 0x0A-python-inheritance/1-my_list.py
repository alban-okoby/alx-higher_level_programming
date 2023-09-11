#!/usr/bin/python3
"""Define a List class"""


class MyList(list):
    """ A subclass of list"""
    def __init__(self):
        """Initializes of list"""
        super().__init__()

    def print_sorted(self):
        """print a sorted of list(ascending order)"""
        print(sorted(self))
