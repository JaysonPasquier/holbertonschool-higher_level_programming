#!/usr/bin/python3
"""Defines a JSON file-reading function."""

import json


def load_from_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)
