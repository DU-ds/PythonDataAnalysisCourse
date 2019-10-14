#!/usr/bin/env python3
import os
import pandas as pd

def suicide_fractions():
    f = os.path.dirname(os.path.realpath(__file__)) + "/who_suicide_statistics.csv"
    df = pd.read_csv(f)
    df["suicides_proportion"] = df.suicides_no / df.population
    country = df.groupby("country")
    return country.suicides_proportion.mean()
    
def suicide_weather():
    f = os.path.dirname(os.path.realpath(__file__)) + "/List_of_countries_by_average_yearly_temperature.html"
    series1 = suicide_fractions()
    lst = pd.read_html(f, index_col = 0, header = 0)
    df = lst[1]     # needed to change to 0 for submission, tests worked for 1 locally 
    # first element is some text
    colname = df.columns[0]
    series2 = df[colname]
    # replace unicode minus with minus pd can understand
    series2 = series2.str.replace("−", "-").astype(float)
    spearman_correlation  = series1.corr(series2, method = "spearman")
    rows_weather = len(series2)
    rows_suicide = len(series1)
    rows_common = len(series1.index.intersection(series2.index))
    return (rows_suicide, rows_weather, rows_common, spearman_correlation)

def main():
    result = suicide_weather()
    print("Suicide DataFrame has {} rows".format(result[0]))
    print("Temperature DataFrame has {} rows".format(result[1]))
    print("Common DataFrame has {} rows".format(result[2]))
    print("Spearman correlation: {}".format(result[3]))

if __name__ == "__main__":
    main()
