#!/usr/bin/python3
"""serialization and deserialization using XML as an
 alternative format to JSON"""

import json
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    This will take a Python dictionary and a filename as parameters.
    It should serialize the dictionary into XML and
    save it to the given filename.
    """
    """creating a root element and iteraring the dictionary into XML"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        """iterating through the dictionary """
        child = ET.SubElement(root, key)
        child.text = str(value)

    """Writing them into XML file"""
    tree = ET.ElementTree(root)
    tree.write(filename, xml_declaration=True)


def deserialize_from_xml(filename):
    """deserilaze data from XML file"""
    """parsing the xml file"""
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
