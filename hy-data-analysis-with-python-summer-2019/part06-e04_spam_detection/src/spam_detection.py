#!/usr/bin/env python3

import os
import gzip
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import metrics

def spam_detection(random_state=0, fraction=1.0):
    f = os.path.dirname(os.path.realpath(__file__))
    file_ham = gzip.open(f + "/ham.txt.gz")
    ham_lst = []
    for line in file_ham:
        ham_lst.append(line)
    nham = int(len(ham_lst) * fraction) # rounds down  
    ham = ham_lst[:nham]
    
    spam_list = []
    file_spam = gzip.open(f + "/spam.txt.gz")
    for line in file_spam:
        spam_list.append(line)
    nspam = int(len(spam_list) * fraction)
    spam = spam_list[:nspam]
    
    pork = ham + spam
    y = np.concatenate([np.ones(nham), np.zeros(nspam)])
    
    count = CountVectorizer(analyzer = "word")
    
    features = count.fit_transform(pork)
    features = features.toarray()
    x1, x2, y1, y2 = train_test_split(features, y, random_state = random_state, train_size = 0.75)
    fm = MultinomialNB()
    fm.fit(x1, y1)
    y_hat = fm.predict(x2)
    score = metrics.accuracy_score(y2, y_hat)
    ntest = len(y2)
    return score, ntest, int(ntest - ntest*score)

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()

"""
In the src folder there are two files: ham.txt.gz and spam.txt.gz. The files are preprocessed versions of the files from https://spamassassin.apache.org/old/publiccorpus/. There is one email per line. The file ham.txt.gz contains emails that are non-spam, and, conversely, emails in file spam.txt are spam. The email headers have been removed, except for the subject line, and non-ascii characters have been deleted.

Write function spam_detection that does the following:

    Read the lines from these files into arrays. Use function open from gzip module, since the files are compressed. From each file take only fraction of lines from the start of the file, where fraction is a parameter to spam_detection, and should be in the range [0.0, 1.0].
    forms the combined feature matrix using CountVectorizer class’ fit_transform method. The feature matrix should first have the rows for the ham dataset and then the rows for the spam dataset. One row in the feature matrix corresponds to one email.
    use labels 0 for ham and 1 for spam
    divide that feature matrix and the target label into training and test sets, using train_test_split. Use 75% of the data for training. Pass the random_state parameter from spam_detection to train_test_split.
    train a MultinomialNB model, and use it to predict the labels for the test set

The function should return a triple consisting of

    accuracy score of the prediction
    size of test sample
    number of misclassified sample po
    """
    