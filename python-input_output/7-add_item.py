#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list,
and then save them to a file:”"""


import sys
import importlib.util

"""load save_to_json_file from 5-save_to_json_file.py"""
spec_save = importlib.util.spec_from_file_location(
    "save_mod", "./5-save_to_json_file.py"
)
save_mod = importlib.util.module_from_spec(spec_save)
spec_save.loader.exec_module(save_mod)
save_to_json_file = save_mod.save_to_json_file

"""load load_from_json_file from 6-load_from_json_file.py"""
spec_load = importlib.util.spec_from_file_location(
    "load_mod", "./6-load_from_json_file.py"
)
load_mod = importlib.util.module_from_spec(spec_load)
spec_load.loader.exec_module(load_mod)
load_from_json_file = load_mod.load_from_json_file


def main():
    """our main function"""
    filename = "add_item.json"
    """loading from jason objects"""
    try:
        "try loading from JSON if the file exists and contains valid data"
        my_objects = load_from_json_file(filename)
    except FileNotFoundError:
        """if the file doesn’t exist, initialize an empty list"""
        my_objects = []

    """extentding the arguemtn counts starting from 1postition  to infinity"""
    my_objects.extend(sys.argv[1:])

    """saving back to the Json file and it overwites it"""
    save_to_json_file(my_objects, filename)
    print(my_objects)

if __name__ == "__main__":
    main()
