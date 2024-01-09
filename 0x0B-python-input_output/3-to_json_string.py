#!/usr/bin/python3
"""
writes serializes a string as JSON file
"""
def to_json_string(my_obj):
    import json
    return (json.dumps(my_obj))

