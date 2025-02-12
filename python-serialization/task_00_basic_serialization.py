#!/usr/bin/env python3
"""Module for basic JSON serialization operations"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file
    Args:
        data: Dictionary to serialize
        filename: Name of the output file
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file
    Args:
        filename: Name of the input file
    Returns:
        Dictionary containing the deserialized data
    """
    with open(filename, 'r') as f:
        return json.load(f)
