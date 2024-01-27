#!/usr/bin/python3

def multiple_returns(sentence):
    # Check if the sentence is empty

    if not sentence:
        return (0, None)

    # Get the length and first character
    length = len(sentence)
    first_char = sentence[0]

    # Return the tuple
    return (length, first_char)
