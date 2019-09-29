#!/usr/bin/env python3

def interleave(*lists):
    lists = list(zip(*lists))
    # for lst in lists:
    l = []
    for lst in lists:
        for e in lst:
            l.append(e)
        # could also do:
        # l.extend(lst)
    return l

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
