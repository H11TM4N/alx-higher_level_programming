#!/usr/bin/python3
def no_c(my_string):
    char = "Cc"
    string = ''.join(i for i in my_string if i not in char)
    return string
