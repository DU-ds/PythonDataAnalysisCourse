#!/usr/bin/env python3

import pandas as pd
import os

def municipalities_of_finland():
    f = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(f + "/municipal.tsv", sep = "\t")
    nrows = df.shape[0]
    end_index = ""
    for i in range(nrows):
        if "Äänekoski" in df["Region 2018"][i]:
            end_index = i
            break
    return df[1:end_index]
    
def main():
    df = municipalities_of_finland()
    print(df.shape)
        
if __name__ == "__main__":
    main()
