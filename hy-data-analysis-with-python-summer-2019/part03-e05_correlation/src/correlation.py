#!/usr/bin/env python3

import scipy.stats as ss
import numpy as np


def load2():
    """This loads the data from the internet. Does not work well on the TMC server."""
    import seaborn as sns
    return sns.load_dataset('iris').drop('species', axis=1).values

def load():
    import pandas as pd
    return pd.read_csv("R:/Git/PythonDataAnalysisCourse/hy-data-analysis-with-python-summer-2019/part03-e05_correlation/src/iris.csv").drop('species', axis=1).values

def lengths():
    df = load()
    sepal_length = df[:,0]
    petal_length = df[:,2]
    r, p = ss.pearsonr(sepal_length, petal_length)
    return r

def correlations():
    df = load()
    return np.corrcoef(df.T)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
