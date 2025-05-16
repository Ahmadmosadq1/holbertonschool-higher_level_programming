#!/usr/bin/python3
def safe_print_division(a, b):
    # Here, we only excute the valid divisions
    try:
        result = a/b
    # If the divigion is by zero, except blcok will be excuted
    except ZeroDivisionError:
        result = None
    # Finally block will be exuted no matter what for both situations
    finally:
        print("Inside result: {}".format(result))
