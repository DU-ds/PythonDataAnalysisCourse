#!/usr/bin/env python3

def distinct_characters(L):
    dikt = {}
    for s in L:
        dikt[s] = len(set(s))
    return dikt

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
