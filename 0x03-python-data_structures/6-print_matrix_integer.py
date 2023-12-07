#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if type(i) != list:
            print("{:d}".format(i))
            continue
        for j in i:
            print("{:d}".format(j), end=" ")
        print()
