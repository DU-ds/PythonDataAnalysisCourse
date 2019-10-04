#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    n, k = a.shape
    col = a[:,c]
    # extract column c to avoid indexing over and over
    # .reshape(1, k)
    # counts = np.unique(col, return_counts = True)
index1, index2 = np.unique(col, return_counts = True)
index1 = index1.reshape(index1.shape[0], 1)
index2 = index2.reshape(index1.shape[0], 1)
index = np.concatenate((index1, index2), axis = 1)
index3, index4 = np.unique(col, return_inverse = True)
    
index = index[np.argsort(index[:,1])]
# index.reshape(n, 1)
a = np.concatenate((a,index), axis = 1)
a = a[a[:,-1].argsort()]
# https://stackoverflow.com/questions/2828059/sorting-arrays-in-numpy-by-column
a = a[:,:k]
    return a

def main():
    c = np.array([[0, 9, 4, 8, 4, 7, 9, 6, 0, 4],
       [0, 4, 2, 4, 3, 7, 7, 7, 5, 0],
       [0, 0, 9, 5, 0, 3, 7, 1, 4, 0],
       [1, 4, 3, 2, 7, 1, 7, 7, 8, 5],
       [6, 5, 5, 5, 1, 0, 0, 0, 4, 5],
       [6, 4, 6, 2, 0, 9, 4, 7, 3, 7],
       [9, 1, 0, 7, 2, 9, 9, 9, 1, 5],
       [9, 9, 0, 3, 9, 8, 8, 0, 6, 1],
       [9, 1, 2, 6, 5, 9, 9, 5, 4, 8],
       [9, 1, 9, 2, 0, 2, 0, 1, 2, 6]])

if __name__ == "__main__":
    main()
    
    
    # https://stackoverflow.com/questions/49496219/sort-list-by-frequency-and-by-value-in-python
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.lexsort.html
d = dict(zip(*np.unique(index4, return_counts = True)))
res = col[np.lexsort((index4, list(map(d.get, index4))))]
