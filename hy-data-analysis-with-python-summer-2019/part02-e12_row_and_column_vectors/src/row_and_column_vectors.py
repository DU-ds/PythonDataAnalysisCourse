#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    rows = []
    ncols = a.shape[1]
    for i in range(a.shape[0]):
        row = a[i,:]
        row = row.reshape(1,ncols)
        rows.append(row)
    return rows

def get_column_vectors(a):
    cols = []
    nrows = a.shape[0]
    for i in range(a.shape[1] ):
        col = a[:,i]
        col = col.reshape(nrows,1)
        cols.append(col)
    return cols

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
