#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    a2 = a * a # a squared
    a2 = np.sum(a2, axis = 1) #sum of squares
    a2 = np.sqrt(a2)
    return a2

def main():
    b = np.arange(12).reshape(3,4)
    print(vector_lengths(b))

if __name__ == "__main__":
    main()
