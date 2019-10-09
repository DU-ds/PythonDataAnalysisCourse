#!/usr/bin/env python3

import os
import pandas as pd

def cyclists():
    f = os.path.dirname(os.path.realpath(__file__)) + "/Helsingin_pyorailijamaarat.csv"
    df = pd.read_csv(f, sep = ";")
    df = df.dropna(axis = 0, how = "all")
    return df.dropna(axis = 1, how = "all")

def main():
    print(cyclists().head())
    
if __name__ == "__main__":
    main()
