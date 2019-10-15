#!/usr/bin/env python3

import os
import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    f = os.path.dirname(os.path.realpath(__file__)) + "/mystery_data.tsv"
    df = pd.read_csv(f, sep = "\t")
    features =  df.iloc[:, :5]
    response = df.iloc[:, -1]
    fm = LinearRegression(fit_intercept=False)
    fm.fit(features, response)
    return fm.coef_

def main():
    coefficients = mystery_data()
    # print the coefficients here
    for i in range(1, 6):
        print(f"Coefficient of X{i} is {coefficients[i-1]}")

if __name__ == "__main__":
    main()
