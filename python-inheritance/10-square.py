#!/usr/bin/python3
"""
Module that defines a Square class.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes square with size.
        """

        # validate size
        self.integer_validator("size", size)

        # call parent constructor
        super().__init__(size, size)

        # private attribute
        self.__size = size
