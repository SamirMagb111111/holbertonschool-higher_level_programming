#!/usr/bin/python3
"""
Module that defines a Rectangle class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes rectangle with width and height.
        """

        # validation
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # private attributes
        self.__width = width
        self.__height = height
