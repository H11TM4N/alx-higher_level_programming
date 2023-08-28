#!/usr/bin/python3
def safe_print_division(a, b):
    result = None  # Initialize result as None

    try:
        result = a / b  # Attempt the division
    except Exception as e:
        print("Inside result: {}".format(result))
    finally:
        if result is not None:
            print("Inside result: {}".format(result))
    return result  # Return the result of the division or None if there was an error
