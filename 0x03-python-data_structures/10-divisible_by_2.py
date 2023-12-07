#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    truth_list = []
    for a in my_list:
        if a % 2 == 0:
            truth_list.append(1)
        else:
            truth_list.append(0)
    return truth_list
