#!/usr/bin/env python3

import os
import pandas as pd

def cyclists():
    f = os.path.dirname(os.path.realpath(__file__)) + "/Helsingin_pyorailijamaarat.csv"
    df = pd.read_csv(f, sep = ";")
    df2 = df.loc[:,df.notnull().any(axis=0)]
    nrows = df2.shape[0]
    return df2.dropna(axis = 1, how = "all")

def main():
    print(cyclists())
    
if __name__ == "__main__":
    main()
