#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list2 = my_list[::-1]
    for i in my_list:
        print("{}".format(my_list2[-i]))
    return 0
