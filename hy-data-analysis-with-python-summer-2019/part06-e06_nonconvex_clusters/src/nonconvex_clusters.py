#!/usr/bin/env python3
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
import os
import pandas as pd
import numpy as np
import scipy
import math
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score

"""
TODO

Also deal with this:
Before submitting the solution, you can plot the data set (with clusters colored) to see what kind of data we are dealing with.
"""

def find_permutation(n_clusters, real_labels, labels):
    if n_clusters == 1:
        return (labels, 0, real_labels)
        # no way to permute 
    permutation = []
    n_outliers = 0
    
    if -1 in np.unique(labels): 
        # outliers
        idx = labels == -1
        
        # count outliers
        n_outliers = sum(idx)
        
        # drop outliers
        real_labels = real_labels[~idx]
        labels = labels[~idx]
        
    
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    logging.debug("permutation: " + str(permutation) + "\nn_outliers: " + str(n_outliers) + "\nlen(real_labels): " + str(len(real_labels)))
    return permutation, n_outliers, real_labels

def nonconvex_clusters():
    f = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(f + "/data.tsv", sep = "\t")
    lst = list()
    X = df.loc[:,["X1", "X2"]]
    y = df.loc[:,"y"]
    for e in np.arange(0.05, 0.2, 0.05):
        fm = DBSCAN(eps = e)
        fm.fit(X)
        n_clusters = len(np.unique(fm.labels_))
        if -1 in fm.labels_:
            n_clusters -= 1 # exclude outlier cluster
        
        new_labels, n_outliers, y2 = find_permutation(n_clusters, y, fm.labels_)
        
        #if(len(np.unique))
        
        
        if len(np.unique(y)) == n_clusters:
            new_labels = [int(new_labels[label]) for label in fm.labels_ if label != -1]
            score = accuracy_score(y2, new_labels)
        #     # except IndexError:
        else:
            score = np.nan
        #     # wrong number of labels 
        lst.append([e, score, float(n_clusters), float(n_outliers)])
    # return lst in dataframe

    return pd.DataFrame(lst, columns = ["eps", "Score", "Clusters", "Outliers"])

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
