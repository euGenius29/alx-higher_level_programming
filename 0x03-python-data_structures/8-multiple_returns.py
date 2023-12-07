#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    first = ""
    if a == 0:
        first += "None"
        return a, first
    else:
        first += sentence[0]
        return a, first
