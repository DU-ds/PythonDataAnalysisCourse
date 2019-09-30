#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    lst = []
    with open(filename, "r") as f:
        l1 = f.readline()
        for li in f:
            lst.append(string_cleaner(li))
    return lst

def string_cleaner(s):
    """
    cleans the individual strings to have format "num\tnum\tnum\tname"
    """
    regex = "(\d*)\s*(\d*)\s*(\d*)\s*(\w*)\n"
    lst = re.findall(regex, s)
    lst = list(lst[0]) #list(tuple)
    return "\t".join(lst)


def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
