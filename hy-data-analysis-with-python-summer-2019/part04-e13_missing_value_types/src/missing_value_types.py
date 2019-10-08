#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    State = ["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"]
    Year_of_independence = [nan, 1917, 1776, 1523, nan, 1992]
    President =[{None, "Niinistö", "Trump", None, "Steinmeier", "Putin"]
    df = pd.DataFrame(index = State)
    df.index.name = "State" #might not be needed
    df["Year of independence"] = Year_of_independence
    df[ "President"] = President
    return df
               
def main():
    return

if __name__ == "__main__":
    main()


