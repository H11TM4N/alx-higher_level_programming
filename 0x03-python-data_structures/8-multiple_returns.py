#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        firstt = None
        length = 0
    else:
        firstt = sentence[0]
        length = len(sentence)
    return length, firstt
