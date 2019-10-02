#!/usr/bin/env python3

import sys

def file_count(filename):
    n_lines = 0
    n_words = 0
    n_characters = 0
    with open(filename, "r") as f:
        for line in f:
            n_lines += 1
            n_characters += len(line)
            n_words += len(line.split())
    return (n_lines, n_words, n_characters)

def main():
    for filename in sys.argv[1:]:
        count = file_count(filename)
        print("%d\t%d\t%d\t%s" %(count[0], count[1], count[2], filename))

if __name__ == "__main__":
    main()
