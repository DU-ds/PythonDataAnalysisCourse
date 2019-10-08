#!/usr/bin/env python3

import os
import pandas as pd

def average_temperature():
    f =os.path.dirname(os.path.realpath(__file__)) + "/kumpula-weather-2017.csv"
    df = pd.read_csv(f)
    is_july = df.m == 7
    july_df = df[is_july]
    return july_df["Air temperature (degC)"].mean()

def main():
    temp = average_temperature()
    print(f"Average temperature in July: {temp:2.1f}")

if __name__ == "__main__":
    main()
