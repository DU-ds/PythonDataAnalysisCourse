#!/usr/bin/env python3

import re
from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    """ counts letters in alphabet
    
    Args:
        a: nx1 np.array of words
    Returns:
        result:
            nx29 np.array, count of letters from alphabet in each word.
            
            alphabet:
            “abcdefghijklmnopqrstuvwxyzäö-“
    
    """
    # write a new preprocessor funtion:
    def custom_preprocessor(s):
        pattern = r"([" + alphabet + "])"
        token_lst = re.findall(pattern, s.lower())
        return "".join(token_lst)
    
    count = CountVectorizer(analyzer = "char", preprocessor = custom_preprocessor, vocabulary = list(alphabet)) # doesn't NEED to be a list, could just be the string
    # dead ends
    # analyzer = "char", strip_accents = "unicode", token_pattern = pattern )
    features = count.fit_transform(a)
    # print(features.shape)
    return features
    # .to_array()
    # part 3 passed 4/5 tests. get_features returns an n x k sparse matrix instead of an n x 29 np array. 
    # Converting to an array gives an array but still n x k. need to tweak how it counts the characters in alphabet
    # https://stackoverflow.com/questions/26576524/how-do-i-transform-a-scipy-sparse-matrix-to-a-numpy-matrix
"""
Part 1.
Write function get_features that gets a one dimensional np.array, 
containing words, as parameter. It should return a feature matrix 
of shape (n, 29), where n is the number of elements of the input array. 
There should be one feature for each of the letters in the following 
alphabet: “abcdefghijklmnopqrstuvwxyzäö-“. The values should be 
the number of times the corresponding character appears in the word.
"""
def contains_valid_chars(s):
    """ checks if all characters in the string are from alphabet -- empty string is true"""
    regex = pattern = r"([" + alphabet + "]*)" # change * to + to make empty sting false
    a = re.fullmatch(regex, s) #returns none if s does not completely match the regex 
    return a != None
    
    """
Part 2.
contains_valid_chars takes a string as a parameter 
returns the truth value of whether all the characters in the string belong to the alphabet or not.
"""

def get_features_and_labels():
    english = load_english()
    finnish = load_finnish()
    finnish_filtered = []
    english_filtered = []
    for word in finnish:
        lword = word.lower()
        if contains_valid_chars(lword):
            finnish_filtered.append(lword)
    for word in english:
        lword = word.lower()
        if lword[0] == word[0]: 
# might not filter words starting with capital letters correctly if two words in string e.g. with hyphen in middle like "core-Python"
            if contains_valid_chars(lword):
                english_filtered.append(lword)
    
    n_eng = len(english_filtered)
    n_fin = len(finnish_filtered)
    y_eng = np.ones(n_eng)
    y_fin = np.zeros(n_fin)
    y = np.concatenate([y_fin, y_eng], axis = 0)
    both = finnish_filtered + english_filtered
    X = get_features(both)
    return (X, y)
"""
Write function get_features_and_labels that returns the tuple (X, y) 
of the feature matrix and the target vector. Use the labels 0 and 1 
for Finnish and English, respectively. Use the supplied functions 
load_finnish() and load_english() to get the lists of words. 
Filter the lists in the following ways:

    Convert the Finnish words to lowercase, and then filter out those 
    words that contain characters that don’t belong to the alphabet.
    
    For the English words first filter out those words that begin with 
    an uppercase letter to get rid of proper nouns. Then proceed as with the Finnish words.

Use get_features function you made earlier to form the feature matrix.
"""

def word_classification():
    x, y = get_features_and_labels()
    fm = MultinomialNB()
    scores = cross_val_score(fm, x, y, cv = model_selection.KFold(n_splits=5, shuffle=True, random_state=0))
    return scores
    
    """
Use the function get_features_and_labels you made earlier to get the 
feature matrix and the labels. Use multinomial naive Bayes to do the 
classification. Get the accuracy scores using the 
sklearn.model_selection.cross_val_score function; use 5-fold cross 
validation. The function should return a list of five accuracy scores.

The cv parameter of cross_val_score can be either an integer, which 
specifies the number of folds, or it can be a cross-validation generator 
that generates the (train set,test set) pairs. What happens if you pass the 
following cross-validation generator to cross_val_score as a parameter: 
sklearn.model_selection.KFold(n_splits=5, shuffle=True, random_state=0).
"""
    


def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
