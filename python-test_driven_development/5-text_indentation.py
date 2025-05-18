#!/usr/bin/python3
"""
This function takes text as an argument, loop through it and if
it it read any of these characters ., ? and :, it will go to the next line
"""


def text_indentation(text):
    """
    a function that goes to newline after ., ? and :

        Args:
        Text: the text to be parised

    Returns:
        None

    Raises:
        "TypeError": if text is not a string type

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for letter in text:
        print(letter, end="")
        if letter in ".?:":
            print()
