#!/usr/bin/env python3

import os
import pandas as pd
import numpy as np
import scipy
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score

"""
TODO

need to figure out how to handle outliers in find_permutation
maybe check tests for a better idea of how to handle it

Also deal with this:
Before submitting the solution, you can plot the data set (with clusters colored) to see what kind of data we are dealing with.

"""

def find_permutation(n_clusters, real_labels, labels):
    if n_clusters == 1: # shouldn't be true
        return (labels, 0)
        # no way to permute, no outliers (otherwise all are "outliers"?)
    permutation = []
    n_outliers = 0
    
    if -1 in np.unique(labels):
        indx = labels == -1
        n_outliers = sum(indx)
        permutation.append(None) # don't know what to do with this 
        # so it's ignored by accuracy_score
        n_clusters -= 1 # one cluster dealt with outside of loop
    
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return (permutation, n_outliers)
    
def nonconvex_clusters():
    # f = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(f + "/data.tsv", sep = "\t")
    lst = list()
    X = df.loc[:,["X1", "X2"]]
    y = df.loc[:,"y"]
    for e in np.arange(0.05, 0.2, 0.05):
        fm = DBSCAN(eps = e)
        fm.fit(X)
        n_clusters = len(np.unique(fm.labels_))
        new_labels, n_outliers = find_permutation(n_clusters, y, fm.labels_)
        if (np.unique(new_labels).all() == np.unique(fm.labels_).all()): #same number of groups 
            new_labels = [new_labels[label] for label in fm.labels_]
            score = accuracy_score(y, new_labels)
            # except IndexError:
        else:
            score = np.nan
            # wrong number of labels 
        lst.append([e, score, n_clusters, n_outliers])
    return lst

    return pd.DataFrame(lst, columns = ["eps", "Score", "Clusters", "Outliers"])

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
