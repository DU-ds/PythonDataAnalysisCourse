#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    """ returns a series with the index and values swapped.
    Assumes the mapping between the index and values of the 
    series is a function with an inverse ie is a bijective function
    """
    index = s.values
    val = s.index
    return pd.Series(val, index)

def main():
    s1 = pd.Series([1,2,3], list("abc"))
    s2 = inverse_series(s1)
    print("Series:")
    print(s1)
    print("Inverse Series:")
    print(s2)
    s = pd.Series([1,2,3,1], index=list("abcd"))
    print(inverse_series(s))
    print("\nNotice the result of duplicated index on accessing Series.")
    print("Using inverse_series(s)[1] gives:")
    print(inverse_series(s)[1])

if __name__ == "__main__":
    main()
