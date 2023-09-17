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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list of dict): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a JSON file.

        Args:
            list_objs (list of Base instances): List of instances to be saved

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            obj_dicts = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(obj_dicts)
            file.write(json_string)
