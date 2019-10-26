#!/usr/bin/env python3

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.decomposition import PCA


def explained_variance():
    f = os.path.dirname(os.path.realpath(__file__)) + "/data.tsv"
    df = pd.read_table(f, sep = '\t')

    # fit model and transform data    
    pc = PCA(df.shape[1])
    pc.fit(df)
    x = pc.transform(df)
    
    # # plots of data before and after change of basis
    # plt.plot(df.iloc[:,0], df.iloc[:,1], "o", c = "red", label = "Before")
    # plt.plot(x[:,0], x[:,1], "o", c = "blue", label = "After")
    # plt.legend()
    # plt.title("Before and After PCA")
    # plt.xlabel("First Variable")
    # plt.ylabel("Second Variable")
    # plt.show()
    
    return list(df.var()), list(pc.explained_variance_) 

def main():
    v, ev = explained_variance()
    print("The variances are:", end = " ")
    for x in v:
        print("%0.3f" % x, end = " ")
    print()
    print("The explained variances after PCA are:", end  = " ")
    for x in ev:
        print("%0.3f" % x, end = " ")
    print()
    
    sums = np.cumsum(ev)
    plt.plot([i for i in range(1, len(sums) + 1)], sums)
    plt.title("Cumulative Sums of the Explained Variance")
    plt.xlabel("Number of terms in the Cumulative Sum")
    plt.ylabel("Cumulative Explained Variance")
    plt.show()

if __name__ == "__main__":
    main()
