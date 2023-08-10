#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    len = len(sys.argv) - 1

    if len == 0:
        print("{} arguments.".format(len))
    elif len == 1:
        print("{} argument:".format(len))
        print("{}: {}".format(len, sys.argv[1]))
    else:
        print("{} arguments:".format(len))
        for i in range(len):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
