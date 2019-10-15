#!/usr/bin/env python3
import os
import numpy as np
import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    f = os.path.dirname(os.path.realpath(__file__)) + "/mystery_data.tsv"
    df = pd.read_csv(f, sep = "\t")
    features =  df.iloc[:, :5]
    response = df.iloc[:, -1]
    fm = linear_model.LinearRegression(fit_intercept=True)
    features = pd.concat([pd.Series(np.ones(features.shape[0])), features], axis = 1)
    fm.fit(features, response)
    result = fm.score(features, response)
    lst = []
    lst.append(result)
    for i in range(1,6):
        fm = linear_model.LinearRegression(fit_intercept=True)
        fm.fit(features.iloc[:, [0, i]], response)
        lst.append(fm.score(features.iloc[:, [0, i]], response))
    return lst

def main():
    coef = coefficient_of_determination()
    print("R2-score with feature(s) X:", coef[0])
    for i in range(1,6):
        print(f"R2-score with feature(s) X{i}: {coef[i]}") 

if __name__ == "__main__":
    main()
