#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    n, two_m = a.shape # int n, even int two_m
    m = two_m//2 # integer
    v1 = np.sum(a[:,:m], axis = 1)
    v2 = np.sum(a[:,m:], axis = 1)
    bool = v1 > v2
    return a[bool,:]

def main():
    np.random.seed(0)
    a = np.random.randint(-10, 10, (5, 6))
    print(a, "\n subset:\n")
    print(first_half_second_half(a))

if __name__ == "__main__":
    main()
