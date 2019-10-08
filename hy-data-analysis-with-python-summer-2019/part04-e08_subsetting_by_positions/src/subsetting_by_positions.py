#!/usr/bin/env python3
import os
import pandas as pd

def subsetting_by_positions():
    f = os.path.dirname(os.path.realpath(__file__)) + "/UK-top40-1964-1-2.tsv"
    df = pd.read_csv(f, sep = "\t")
    return df.iloc[:10,2:4]

def main():
    print(subsetting_by_positions())


if __name__ == "__main__":
    main()
