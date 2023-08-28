#!/usr/bin/python3

def raise_exception():
    try:
        raise TypeError("A custom type exception")
    except TypeError as error:
        print("Exception raised: ", error)
