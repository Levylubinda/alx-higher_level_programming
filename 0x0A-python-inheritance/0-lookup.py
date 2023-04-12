#!/usr/bin/python3
""" Returns the list of available thingis
    attributes and methods of an object.
"""


def lookup(obj):
    """ Return the list of available attributes """
    return dir(obj)
