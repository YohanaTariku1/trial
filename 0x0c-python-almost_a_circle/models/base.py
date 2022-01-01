#!/usr/bin/python3
"""Module that represent base model class"""
import json
import csv
import turtle

class Base:
    """Base model representation
    
        Attributes:
            __nb__objects (int): number of bases
    """

    __nb__objects = 0

    def __init__(self, id=None):
        """
        Initialize class
        
            Args:
                id (int): The identity of the new base
        """

        if id is not None:
            self.id = id
        else:
         Base.__nb__objects += 1
         self.id = Base.__nb__objects



    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)