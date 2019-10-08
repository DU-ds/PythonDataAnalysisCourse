#!/usr/bin/env python3

import os
import pandas as pd

def below_zero():
    f = os.path.dirname(os.path.realpath(__file__)) + "/kumpula-weather-2017.csv"
    df = read_csv(f)
    return sum(df["Air temperature (degC)"] < 0)

def main():
    n_days = below_zero()
    print(f"Number of days below zero: {n_days:2d}")

if __name__ == "__main__":
    main()
