#!/usr/bin/python3
"""Module that defines a Rectangle class."""


class Rectangle:
    """Class that defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # ... digər kodlar eyni qalır ...

    @staticmethod
    def biggerorequal(rect_1, rect_2):
        """Return the bigger rectangle based on area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
