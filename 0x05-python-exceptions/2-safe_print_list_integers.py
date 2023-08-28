#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_elts = 0
    for v in range(0, x):
        try:
            int_value = my_list[i]
            print("{:d}".format(int_value), end="")
            printed_elts += 1
        except (ValueError, TypeError):
            continue
    print()
    return (printed_elts)
