#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    lent = len(sys.argv) - 1

    if lent == 0:
        print("{} arguments.".format(lent))
    elif lent == 1:
        print("{} argument:".format(lent))
        print("{}: {}".format(lent, sys.argv[1]))
    else:
        print("{} arguments:".format(lent))
    for i in range(lent):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
