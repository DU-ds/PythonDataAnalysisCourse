#!/usr/bin/env python3
import os
import pandas as pd

def subsetting_with_loc():
    f = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(f + "/municipal.tsv", sep = "\t", index_col = "Region 2018")
    cols = ["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]
    return df["Akaa":"Äänekoski"].loc[:,cols]

def main():
    print(subsetting_with_loc().head())
    return

if __name__ == "__main__":
    main()
