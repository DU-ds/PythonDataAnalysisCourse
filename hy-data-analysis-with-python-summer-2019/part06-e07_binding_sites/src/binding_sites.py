#!/usr/bin/env python3

import os
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

def toint(x):
    x = x.replace("A", 0)
    x = x.replace("C", 1)
    x = x.replace("G", 2)
    x = x.replace("T", 3)
    return x

def get_features_and_labels(filename):
    #read data in
    f = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(f + filename, sep = "\t")
    
    # transform the string X column to a feature matrix
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.extractall.html#pandas.Series.str.extractall
    regex = r"([ACGT])" * 8
    feature_matrix = df.X.str.extractall(regex)
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html#pandas.Series.apply
    feature_matrix = feature_matrix.apply(toint)
    return (feature_matrix, df.y)
    
    return (np.array([[]]), np.array([]))

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):
    # get data ready
    features, labels = get_features_and_labels(filename)
    #fit model and predict values
    y_hat = AgglomerativeClustering(n_clusters = 2, affinity = "euclidean", linkage = "average").fit_predict(features)
    # return accuracy score
    return accuracy_score(labels, y_hat)

def cluster_hamming(filename):
    # get data ready
    features, labels = get_features_and_labels(filename)
    #fit model and predict values  -- compute distance first then use distance in model
    ## compute distance
    dist = pairwise_distances(feature_matrix, metric = "hamming")
    ## fit model
    y_hat = AgglomerativeClustering(n_clusters = 2, affinity = "precomputed", linkage = "average").fit_predict(dist)
    # plot distances
    plot(dist) #shows four square clusters, which seems to make sense -- dna has 4 nucleotides
    # return accuracy score
    return accuracy_score(labels, y_hat)

 ###TODO fix labels for distance functions using the find_permutation function
 # Note that you may have to use the find_permutation function again, 
 # because even though the clusters are correct, they may be labeled 
 # differently than the real labels given in data.seq.

def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("/data.seq"))


if __name__ == "__main__":
    main()
