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
    
    count = CountVectorizer(analyzer = "char", preprocessor = custom_preprocessor)
    # dead ends
    # analyzer = "char", strip_accents = "unicode", token_pattern = pattern )
    features = count.fit_transform(finnish)
    return np.array([[]])
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
    return True
    """
Part 2.
contains_valid_chars takes a string as a parameter 
returns the truth value of whether all the characters in the string belong to the alphabet or not.
"""

def get_features_and_labels():
    return np.array([[]]), np.array([])
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
    return []


def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
