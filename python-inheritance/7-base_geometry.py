#!/usr/bin/python3
"""
Module that defines a BaseGeometry class.
"""


class BaseGeometry:
    """
    BaseGeometry class with area and integer validation.
    """

    def area(self):
        """
        Raises an exception indicating that area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
