#!/usr/bin/python3
""" module Square """


class Square:
    """
    defines Square by private instance attribute: size
    """
    def __init__(self, size=0):
        """
        initializes square objects,
        size must be an integer and greater than 0
        """
        self.__size = size
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        calculates the area of the current square
        """
        return (self.__size) ** 2
