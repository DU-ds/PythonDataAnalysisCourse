#!/usr/bin/env python3

def find_matching(L, pattern):
    lst = []
    for i, v in enumerate(L):
        if pattern in v:
            lst.append(i)
    return lst

def main():
    find_matching(["sensitive", "engine", "rubbish", "comment"], "en")

if __name__ == "__main__":
    main()
