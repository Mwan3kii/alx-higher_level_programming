#!/usr/bin/env python3
import sys
from save_to_json_file_5 import save_to_json_file
from load_from_json_file_6 import load_from_json_file
def add_items_to_list(arguments):
    existing_list = load_from_json_file("add_item.json", default=[])
    existing_list.extend(arguments)
    save_to_json_file(existing_list, "add_item.json")
