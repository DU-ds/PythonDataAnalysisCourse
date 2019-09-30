#!/usr/bin/env python3

def sum_equation(L):
    """takes a list of positive integers as parameters and returns a string with an equation of the sum of the elements"""
    if len(L) == 0:
        return "0 = 0"
    total = sum(L)
    l = list(map(str, L))
    s = " + ".join(l) 
    s += " = " + str(total)
    return s

def main():
    pass

if __name__ == "__main__":
    main()
