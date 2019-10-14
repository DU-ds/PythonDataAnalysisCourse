#!/usr/bin/env python3
import os
import pandas as pd

def suicide_fractions():
    f = os.path.dirname(os.path.realpath(__file__)) + "/who_suicide_statistics.csv"
    df = pd.read_csv(f)
    df["suicides_proportion"] = df.suicides_no / df.population
    country = df.groupby("country")
    return country.suicides_proportion.mean()
    

def main():
    print(suicide_fractions())

if __name__ == "__main__":
    main()
