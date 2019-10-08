#!/usr/bin/env python3

import pandas as pd
def municipalities_of_finland():
    f = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(f + "/municipal.tsv", sep = "\t")
    nrows = df.shape[0]
    end_index = ""
    for i in range(nrows):
        if "Äänekoski" in df["Region 2018"][i]:
            end_index = i
            break
    return df[1:end_index]
    
def swedish_and_foreigners():
    df = municipalities_of_finland()
    sweed_bool = df['Share of Swedish-speakers of the population, %'] > 5
    forn_bool = df['Share of foreign citizens of the population, %'] > 5
    three_cols = df[['Population', 'Share of Swedish-speakers of the population, %', 'Share of foreign citizens of the population, %']]
    return three_cols[forn_bool & sweed_bool]

def main():
    return

if __name__ == "__main__":
    main()

"""
Write function swedish_and_foreigners that

    Reads the municipalities data set
    Takes the subset about municipalities (like in previous exercise)
    Further take a subset of rows that have proportion of Swedish speaking people and proportion of foreigners both above 5 % level
    From this data set take only columns about population, the proportions of Swedish speaking people and foreigners, that is three columns.

The function should return this final DataFrame.

Do you see some kind of correlation between the columns about Swedish speaking and foreign people? Do you see correlation between the columns about the population and the proportion of Swedish speaking people in this subset?
"""
