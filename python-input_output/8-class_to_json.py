#!/usr/bin/python3
"""
Module that defines class_to_json function
"""


def class_to_json(obj):
    """Returns description with simple data
    structure for JSON serialization"""
    return obj.__dict__
