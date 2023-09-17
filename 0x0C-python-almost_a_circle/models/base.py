#!/usr/bin/python3
"""Define a Base class"""


class Base:
    """
    Base class for managing unique IDs in derived classes

    Attributes:
        __nb_objects (int): A private class attribute to
        keep track of the number of instances
        id (int): A public instance attribute representing
        the unique ID of an object

    Methods:
        __init__(self, id=None): Constructor for the Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): An optional integer ID. If provided,
            it sets the object's ID to the given value.
                If not provided, it increments the __nb_objects counter
                and assigns a unique ID.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
