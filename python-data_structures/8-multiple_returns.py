#!/usr/bin/python3
def multiple_returns(sentence):
    # if thr sentence is not empty
    str_length = len(sentence)

    if str_length == 0:
        first_char = None
    else:
        first_char = sentence[0]
    # we tuple over a list since tuple accepts only  argument
    return (str_length, first_char)
    