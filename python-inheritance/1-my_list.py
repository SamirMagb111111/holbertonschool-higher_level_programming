#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
and provides a method to print the list sorted.
"""


class MyList(list):
    """
    MyList is a subclass of list that adds a print_sorted method.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order without modifying it.
        """
        print(sorted(self))
