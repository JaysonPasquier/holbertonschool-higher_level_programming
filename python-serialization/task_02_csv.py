#!/usr/bin/env python3
"""Module for converting CSV data to JSON format"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV file to JSON format and save to data.json
    Args:
        csv_filename: Name of the input CSV file
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Read CSV file and convert to list of dictionaries
        with open(csv_filename, 'r') as csv_file:
            csv_data = list(csv.DictReader(csv_file))

        # Write JSON data to file
        with open('data.json', 'w') as json_file:
            json.dump(csv_data, json_file, indent=4)

        return True

    except Exception:
        return False
