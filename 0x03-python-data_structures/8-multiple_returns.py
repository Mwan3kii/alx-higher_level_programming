#!/usr/bin/python3
def multiple_returns(sentence):
    num = len(sentence)
    if not sentence:
        char = None
    else:
        char = sentence[0]
    return num, char
