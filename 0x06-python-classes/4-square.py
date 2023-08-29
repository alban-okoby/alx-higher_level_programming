#!/usr/bin/python3



class Square:
    def __init__(self, size=0):
        """Initialize a square with a given size."""
        self.__size = size

    @property
    def size(self):
        """Getter method for size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

