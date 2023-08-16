#!/usr/bin/python3
def uniq_add(my_list=[]):
    filtered = list(set(my_list))
    total = 0
    for i in filtered:
        total = total + i
    return total
