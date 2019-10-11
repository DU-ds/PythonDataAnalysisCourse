#!/usr/bin/env python3
import os
import pandas as pd

def top_bands():
    f = os.path.dirname(os.path.realpath(__file__))
    fourty = pd.read_csv(f + "/UK-top40-1964-1-2.tsv", sep = "\t").astype("object")
    bands = pd.read_csv(f + "/bands.tsv", sep = "\t")
    # bands.Band is Title Case,
    # fourty.Artist is UPPER CASE
    # fourty.Artist = fourty.Artist.str.title() 
    # for some reason this capitalizes words
    # e.g. one and two ==> One And Two -- instead of One and Two
    
    bands.Band = bands.Band.str.upper()
    return pd.merge(bands, fourty, left_on = "Band", right_on = "Artist", how = "left")

def main():
    print(top_bands())

if __name__ == "__main__":
    main()
