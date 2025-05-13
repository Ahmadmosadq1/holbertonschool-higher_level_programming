def no_c(my_string):
    # Strings are not mutable so we have to enumerate the string
    # enumarte will turn each element to a tuple of (indx, element)
    # so we will use idx and char for looping
    new_string = ""
    for idx, char in enumerate(my_string):
        if char == "c" or char == "C":
            continue
        else:
            # concate the new string without c or C
            new_string += char
    return new_string
