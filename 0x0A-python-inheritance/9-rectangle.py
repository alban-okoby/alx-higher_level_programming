#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle who inherite of BaseGeometry class"""

    def __init__(self, width, height):
        """Intialize a new Rectangle
        Args:
            width (int): The width of the new Rectangle
            height (int): The height of the new Rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

        def area(self):
            """Return the area of the rectangle"""
            return self.__width * self.__height

        def __str__(self):
            """Return print() and str() of rectangle"""
            strg = "[" + str(self.__class__.__name__) + "] "
            strg += str(self.__width) + "/" + str(self.__height)
            return strg
