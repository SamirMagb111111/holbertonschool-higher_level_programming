#!/usr/bin/env python3
"""
Module that defines Shape and related classes.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for shapes.
    """

    @abstractmethod
    def area(self):
        """
        Calculate area.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate perimeter.
        """
        pass


class Circle(Shape):
    """
    Circle class.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculate circle area.
        """
        return 3.141592653589793 * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate circle perimeter.
        """
        return 2 * 3.141592653589793 * self.radius


class Rectangle(Shape):
    """
    Rectangle class.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate rectangle area.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate rectangle perimeter.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of shape.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
