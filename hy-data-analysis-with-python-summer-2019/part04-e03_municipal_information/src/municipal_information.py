#!/usr/bin/env python3

import pandas as pd
import os

def main():
    f = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(f + "/municipal.tsv", sep = "\t")
    r,c = df.shape
    print("Shape: " + str(r) + "," + str(c))
    print("Columns:")
    for col in df.columns:
        print(col)


if __name__ == "__main__":
    main()
