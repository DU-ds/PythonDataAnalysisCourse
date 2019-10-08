#!/usr/bin/env python3

import os
import pandas as pd

def cyclists():
    f = os.path.dirname(os.path.realpath(__file__)) + "/Helsingin_pyorailijamaarat.csv"
    df = read_csv(f)
    df2 = df[df.notnull().any(axis=0)]
    nrows = df2.shape[0]
    return df2.dropna(axis = 1, how = "all")

def main():
    return
    
if __name__ == "__main__":
    main()
