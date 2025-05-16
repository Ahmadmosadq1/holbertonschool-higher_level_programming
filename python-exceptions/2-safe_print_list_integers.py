#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for element in range(x):
        # we loop through the list and print all the integers
        try:
            print("{:d}".format(my_list[element]), end="")
            count += 1
        # in case we encounted a value/type errors, we skip it
        except (ValueError, TypeError):
            continue
        # If the index is out of range, we break out of the loop
        except IndexError:
            break
    print()
    return count
