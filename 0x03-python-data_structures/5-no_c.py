#!/usr/bin/python3
def no_c(my_string):
    res = ""
    for c in my_string:
        if c not in ['c', 'C']:
            res += c
    return res
