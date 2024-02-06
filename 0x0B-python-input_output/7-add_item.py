#!/usr/bin/python3
"""Tsk module seven."""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg_list = list(sys.argv[1:])

try:
    existing_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    existing_list = []
    
existing_list.extend(arg_list)
save_to_json_file(existing_list, 'add_item.json')
