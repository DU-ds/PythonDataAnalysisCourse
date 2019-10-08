#!/usr/bin/env python3

import pandas as pd
import os

def snow_depth():
    f = os.path.dirname(os.path.realpath(__file__)) + "/kumpula-weather-2017.csv"
    df = pd.read_csv(f)
    return df["Snow depth (cm)"].max()

def main():
    depth = snow_depth()
    print(f"Max snow depth: {depth:2.1f}")

if __name__ == "__main__":
    main()
