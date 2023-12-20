#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    count = 0
    printed_anything = False

    try:
        for i in range(x):
            if isinstance(my_list[i], int:
                print("{:d}".format(my_list[i], end="")
                count += 1
                printed_anything = True

        if printed_anything:
        print()
    except IndexError:
        pass

    return count

