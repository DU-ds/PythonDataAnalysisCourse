#!/usr/bin/env python3
import os
import pandas as pd
import numpy as np


def cleaning_data():
    f = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(f + "/presidents.tsv", sep = "\t")
    df.Start = df.Start.replace(r"([0-9]*)\s+[a-zA-Z]+", r"\1", regex = True)
    df.President = df.President.replace(r"([a-zA-Z]*),\s+([a-zA-Z]*)", r"\2 \1" , regex = True)
    df["Vice-president"] = df["Vice-president"].replace(r"([a-zA-Z]*),\s+([a-zA-Z]*)", r"\2 \1" , regex = True)
    df["Vice-president"] = df["Vice-president"].str.title()
    df["Seasons"] = df["Seasons"].replace(r"(two)", "2", regex = True)
    df["Seasons"] = df["Seasons"].map(int)
    df["Start"] = df.Start.map(int)
    df["Last"] = pd.to_numeric(df["Last"], errors = "coerce")
    return df

def amendment_22_check(s):
    return s == 1 or s == 2

def comma_check(s):
    """ true if there is no comma in the string s"""
    return not ("," in s)
    
# def comma_response(matchobj):
#     """fixes input string, assumes string format: lastname, firstname"""
#     s.replace(",", "")
#     lst = s.split()
#     firstname = lst[-1]
#     lastname = lst[0]
#     return firstname.capitalize() + " " + lastname.capitalize()

def comma_response(matchobj):
    """takes (match object from regex method), outputs string with names reversed assumes string of match object is in format: lastname, firstname"""
    # https://docs.python.org/3/library/re.html#re.sub
    return matchobj.group(2).capitalize() + " " + matchobj.group(1).capitalize()

def amendment_22_response(s):
    if s == "one":
        return 1
    if s == "two":
        return 2
    

def main():
    print(cleaning_data())
    return

if __name__ == "__main__":
    main()
