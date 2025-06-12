#!/usr/bin/python3
"""reading data from one format (CSV) and converting it into
another format (JSON) using serialization techniques"""


import csv
import json


def convert_csv_to_json(filename):
    """convering csv format to json format"""
    try:
        with open(filename, newline='') as csvf:
            """reader just conerts data to dictionaries"""
            reader = csv.DictReader(csvf)
            """
            we have to list these dictionaries to be indexed and extracted
            """
            data = list(reader)
        """opening a file to dump data to"""
        with open("data.json", 'w') as jsonf:
            json.dump(data, jsonf)
        return True
    except FileNotFoundError:
        return False
