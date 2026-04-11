#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list and
adds a method to print the list in sorted order.
"""


class MyList(list):
    """
    MyList is a subclass of list that provides additional functionality.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order without
        modifying the original list.
        """
        print(sorted(self))
