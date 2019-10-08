#!/usr/bin/env python3

import os
import numpy as np
import pandas as pd

def growing_municipalities(df):
    return sum(df.loc[:,'Population change from the previous year, %'] > 0)/df.shape[0]

def municipalities():
    f = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(f + "/municipal.tsv", sep = "\t", index_col = "Region 2018")
    return df

def main():
    df = municipalities()
    rand = np.random.randint(-50, 100, df.shape[0])
    bool = rand >= 0
    subset = df[bool]
    p = growing_municipalities(subset)
    print(f"Proportion of growing municipalities: {p:.1f}%")

if __name__ == "__main__":
    main()

"""

Write function growing_municipalities that gets subset of municipalities (a DataFrame) as a parameter and returns the proportion of municipalities with increasing population in that subset.

Test your function from the main function using some subset of the municipalities. Print the proportion as percentages using 1 decimal precision.

Example output:

Proportion of growing municipalities: 12.4%

"""