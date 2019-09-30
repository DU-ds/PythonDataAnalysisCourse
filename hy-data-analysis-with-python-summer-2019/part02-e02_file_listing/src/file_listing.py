#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    """
    Args:
        filename: string
            file with file information (think ls -l)
    Returns:
        lst: list
            contains tuples (size, month, day, hour, minute, filename)
    """
    lst = []
    with open(filename, "r") as f:
        for li in f:
            lst.append(file_regex(li))
    return lst
        
def file_regex(line):
    """takes a line, parses it, returns the tuple needed by file_listing"""
        # (size, month, day, hour, minute, filename)
    regex = r"[-rwxd]{9}\s\d+\s\w*\s[a-zA-Z0-9\-]*\s*(\d*)\s(\w{3})\s+(\d{1,2})\s(\d{2})\:(\d{2})\s([^\n]+)"#\n"
    lst = re.findall(regex, line)
    t = lst[0]
    lst = [int(t[0]), t[1], int(t[2]), int(t[3]), int(t[4]), t[5]]
    t = tuple(lst) 
    return t

def main():
    pass

if __name__ == "__main__":
    main()
