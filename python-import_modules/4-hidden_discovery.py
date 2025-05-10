#!/usr/bin/python3

import importlib.util
import sys


def hidden_discovery():
    # we first load the compiled module froma /tmp/ path
    spec = importlib.util.spec_from_file_location("hidden_4", "/tmp/hidden_4.pyc")
    hidden = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden)

    # Extracting all the names defined in that bytecode file
    names = dir(hidden)
    # we now filter out any string starts with '__'
    # if it was found, the if conditon will be True and with not, it skips
    # if it was false, with 'not', it will be True and print them
    filter_out = [n for n in names if not n.startswith("__")]
    # sorting the names:
    filter_out.sort()
    # Now, we print each name in a line
    for line in filter_out:
        print("{}".format(line))


if __name__ == "__main__":
    hidden_discovery()
