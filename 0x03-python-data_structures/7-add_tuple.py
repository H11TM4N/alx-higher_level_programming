#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first = tuple_a + (0, 0)[:2 - len(tuple_a)]
    second = tuple_b + (0, 0)[:2 - len(tuple_b)]

    # Calculate sum of corresponding elements
    sum_first = first[0] + second[0]
    sum_second = first[1] + second[1]

    # Return the result as a tuple
    result = (sum_first, sum_second)
    return result
