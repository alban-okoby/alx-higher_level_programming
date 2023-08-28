#!/usr/bin/python3

def raise_exception():
    try:
        raise TypeError("Exception raised")
    except TypeError as error:
        print(error)
