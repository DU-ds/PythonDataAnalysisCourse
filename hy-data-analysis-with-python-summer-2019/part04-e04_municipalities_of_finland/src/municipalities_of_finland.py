#!/usr/bin/env python3

import pandas as pd
import os

def municipalities_of_finland():
    f = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(f + "/municipal.tsv", sep = "\t", index_col = "Region 2018")
    return df["Akaa":"Äänekoski"]
    
def main():
    df = municipalities_of_finland()
    print(df.shape)
        
if __name__ == "__main__":
    main()
