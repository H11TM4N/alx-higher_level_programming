#!/usr/bin/python3

def add(args):
    result = 0
    for i in args:
        try:
            num = int(i)
            result = result + num
        except ValueError:
            print("Invalid argument")
    return result


if __name__ == "__main__":
    import sys

    arg = sys.argv[1:]

    res = add(arg)
    print("{}".format(res))
