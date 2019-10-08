#!/usr/bin/env python3

import os
import pandas as pd
import numpy as np

def special_missing_values():
    f = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(f + "/UK-top40-1964-1-2.tsv", sep = "/t")
    is_new = df["LW"] == "New"
    is_re = df["LW"] == "Re"
    either = is_new | is_re
    df.loc[either, "LW"] = None
    df = df.dropna(axis = 0)
    df["LW"].astype(str).astype(np.int64)
    # converting to str not always needed
    diff =  df["LW"] - df["Pos"]
    dropped = diff < 0
    return df[dropped,:]
    
    
def main():
    return

if __name__ == "__main__":
    main()
"R:/Git/PythonDataAnalysisCourse/hy-data-analysis-with-python-summer-2019/part04-e14_special_missing_values/src/UK-top40-1964-1-2.tsv"