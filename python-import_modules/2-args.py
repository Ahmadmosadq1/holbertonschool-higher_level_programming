#!/usr/bin/python3
import sys


def display_args():
    # Importing Sys library so we can use argv method starts from 0
    args = sys.argv[1:]
    # counting the number of arguments passed in the shell by the user
    argc = len(sys.argv) - 1
    # After couinting the args, we put(number argument/s)
    if argc == 0:
        print("{} arguments:".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
    elif argc > 1:
        print("{} arguments:".format(argc))
    # we here used enumrate to have a tuple like (index, count)
    # so we can fill them inside the formar
    for index, count in enumerate(args):
        print("{}: {}".format(index, count))


if __name__ == "__main__":
    display_args()
