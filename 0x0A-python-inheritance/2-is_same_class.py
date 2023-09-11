#!/usr/bin/python3

def is_same_class(obj, a_class):
    """Use the type() function to get the class of the object"""
    the_obj_class = type(obj)
    return the_obj_class == a_class
