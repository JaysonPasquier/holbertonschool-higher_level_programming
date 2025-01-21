#!/usr/bin/python3

"""
This module defines a function that prints a name using the format:
'My name is <first_name> <last_name>'.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".
    Raises a TypeError if either argument is not a string.

    Args:
        first_name (str): The first name
        last_name  (str): The last name (optional)
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name == "":
        print(f"My name is {first_name}")
    else:
        print(f"My name is {first_name} {last_name}")
