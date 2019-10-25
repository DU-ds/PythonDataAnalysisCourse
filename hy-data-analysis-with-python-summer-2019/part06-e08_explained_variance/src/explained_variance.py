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
    
    pc = PCA(df.shape[1])
    pc.fit(df)
    x = pc.transform(df)
    plt.scatter(df.iloc[:,0], df.iloc[:,1])
    plt.scatter(x[:,0], x[:,1])
    
    
    return list(df.var()), list(pc.explained_variance_) 

def main():
    v, ev = explained_variance()
    print("The variances are:", end = " ")
    for x in v:
        print("%0.3f" % x, end = " ")
    print("The explained variances after PCA are:", end  = " ")
    for x in ev:
        print("%0.3f" % x, end = " ")
    print(sum(v), sum(ev))

if __name__ == "__main__":
    main()
