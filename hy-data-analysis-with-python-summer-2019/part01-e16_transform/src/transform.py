#!/usr/bin/env python3

def transform(s1, s2):
    l1 = map(int,s1.split())
    l2 = map(int,s2.split())
    lst = zip(l1,l2)
    lst = list(map(lambda x : x[1] * x[0], lst))
    return lst


def main():
    pass

if __name__ == "__main__":
    main()
