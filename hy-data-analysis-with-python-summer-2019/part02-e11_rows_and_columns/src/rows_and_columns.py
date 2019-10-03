#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    """
    Args:
        a: 2-d numpy array
    Returns:
        rows: list of 1-d numpy arrays, rows of a
    """
    rows = []
    for i in range(a.shape[0]):
        rows.append(a[i,:])
    return rows

def get_columns(a):
    """
    Args:
        a: 2-d numpy array
    Returns:
        cols: list of 1-d numpy arrays, columns of a
    """
    cols = []
    for i in range(a.shape[1]):
        cols.append(a[:,i])
    return cols

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
