#!/usr/bin/python3
""" Module that defines the class Student
"""


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ instantiation method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ method that returns dir description """
        return self.__dict__.copy()
