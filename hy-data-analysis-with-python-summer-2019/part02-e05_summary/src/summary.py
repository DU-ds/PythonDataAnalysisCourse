#!/usr/bin/env python3

import sys
import math

def summary(filename):
    lst = []
    with open(filename, "r") as f:
        for line in f:
            try:
                line = float(line)
                lst.append(line)
            except ValueError:
                pass# ignore it 
        total = sum(lst)
        xbar = total/(len(lst))
        lst = list(map(lambda x: (x - xbar)**2, lst))
        sd = math.sqrt(sum(lst)/(len(lst)-1))
    return (total,xbar,sd)

def main():
    for i in range(1, len(sys.argv)):
        su = summary(sys.argv[i])
        print("File: %s Sum: %.6f Average: %.6f Stddev: %.6f" % (sys.argv[i], su[0], su[1], su[2]))

if __name__ == "__main__":
    main()
