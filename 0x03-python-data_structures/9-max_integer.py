#!/usr/bin/python3
def max_integer(my_list=[]):
    high = my_list[0]
    for i in my_list:
        if i > high:
            high = i
    if len(my_list) == 0:
        return None
    else:
        return high
