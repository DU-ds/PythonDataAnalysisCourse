#!/usr/bin/env python3

import os
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    n_outliers = 0
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        if new_label == -1:
            new_label = None
            n_outliers += 1
        else:
            permutation.append(new_label)        
    return (permutation, n_outliers)

def nonconvex_clusters():
    f = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(f + "/data.tsv", sep = "\t")
    lst = []
    for e in np.arange(0.05, 0.2, 0.05):
fm = DBSCAN(eps = e)
fm.fit(df.loc[:,["X1", "X2"]])
n_clusters = len(np.unique(fm.labels_))
new_labels, n_outliers = find_permutation(n_clusters, df.loc[:,"y"], fm.labels_)
new_labels = [new_labels[label] for label in fm.labels_]
score = accuracy_score(df.loc[:,"y"], new_labels)
lst.append(())
        
    return pd.DataFrame()

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
