#!/usr/bin/python3

def lookup(obj):
    """Use the dir() function to get the list of attributes and methods"""
    attr_and_methods = dir(obj)
    filtered = [i for i in attr_and_methods if not i.startswith('__')]
    return (filtered)
