#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    a = np.arange(n).reshape(n, 1)
    b = np.arange(n)
    try:
        c = b * a
    except:
        print("oops")
    return c

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
