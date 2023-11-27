#!/usr/bin/python3
"""
This module defines a function that prints a person's name.
"""


def print_name(first_name, last_name=""):
    """Prints the name of a person.

    Args:
        first_name: The first name of the person.
        last_name: The last name of the person. Default value is an empty string.

    Returns:
        None

    Raises:
        TypeError: If first_name or last_name is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
