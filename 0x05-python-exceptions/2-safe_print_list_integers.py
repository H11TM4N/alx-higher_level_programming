#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            if count >= x:
                raise ValueError("x is bigger than the length of my_list")
            try:
                converted_i = "{:d}".format(int(i))
                print(converted_i, end="")
                count += 1
            except (ValueError, TypeError):
                pass

    except ValueError as ve:
        print("Value error")

    print()
    return count
