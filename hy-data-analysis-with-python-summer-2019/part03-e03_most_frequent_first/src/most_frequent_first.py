#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    n, k = a.shape
    col = a[:,c]
    # extract column c to avoid indexing over and over
    # .reshape(1, k)
    # counts = np.unique(col, return_counts = True)
    index = np.unique(col, return_inverse = True)[1]
    index = index.reshape(n, 1)
    a = np.concatenate((a,index), axis = 1)
    a = a[a[:,-1].argsort()]
    # https://stackoverflow.com/questions/2828059/sorting-arrays-in-numpy-by-column
    a = a[:,:k]
    return a

def main():
    pass

if __name__ == "__main__":
    main()
    
    
    
