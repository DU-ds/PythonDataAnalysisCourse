#!/usr/bin/env python3
import os
import pandas as pd

def best_record_company():
    f = os.path.dirname(os.path.realpath(__file__)) + "/UK-top40-1964-1-2.tsv"
    df = pd.read_csv(f, sep = "\t")
    records = df.groupby("Publisher")
    total_weeks = records.WoC.sum()
    best = max(total_weeks)
    for i, v in enumerate(total_weeks):
        if v == best:
            break # found it!
    best_record = total_weeks.index[i]
    return df.loc[df.Publisher == best_record,:]
    

def main():
    print(best_record_company())
    

if __name__ == "__main__":
    main()
