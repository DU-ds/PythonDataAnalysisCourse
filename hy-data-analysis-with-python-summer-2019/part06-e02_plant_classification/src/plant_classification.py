#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics

def plant_classification():
    df = load_iris()
    x1, x2, y1, y2 = train_test_split(df.data, df.target, random_state = 0, test_size = 0.2)
    fm = naive_bayes.GaussianNB()
    fm.fit(x1, y1)
    y_hat = fm.predict(x2)
    return metrics.accuracy_score(y2, y_hat)
    """
Write function plant_classification that does the following:
    loads the iris dataset using sklearn (sklearn.datasets.load_iris)
    splits the data into training and testing part using the train_test_split function so that the training set size is 80% of the whole data (give the call also the random_state=0 argument to make the result deterministic)
    use Gaussian naive Bayes to fit the training data
    predict labels of the test data
    the function should return the accuracy score of the prediction performance (sklearn.metrics.accuracy_score)
    """

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
