#!/usr/bin/env python3
import os
import pandas as pd

def cyclists():
    f = os.path.dirname(os.path.realpath(__file__)) + "/Helsingin_pyorailijamaarat.csv"
    df = pd.read_csv(f, sep = ";")
    df = df.dropna(axis = 0, how = "all")
    return df.dropna(axis = 1, how = "all")

"""def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]

    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d
"""
def split_date(df):
    df = df.Päivämäärä.str.split(expand = True)
    colnames = ["Weekday", "Day", "Month", "Year", "Hour"]
    df.columns = colnames
    old_week = ["ma", "ti", "ke", "to", "pe", "la", "su"]
    week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i in range(len(week)):
        df.Weekday = df.Weekday.str.replace(old_week[i], week[i])
    months = ["tammi", "helmi", "maalis", "huhti", "touko", "kesä", "heinä", "elo", "syys", "loka", "marras", "joulu"] 
    i = 1
    for i in range(0, len(months)):
        df.Month = df.Month.replace(months[i], i+1)
    df.Month = pd.to_numeric(df.Month.map(int), downcast = "integer")
    df.Hour = df.Hour.str.extract(r"([0-9]*)", expand = False)
    df.Hour = df.Hour.map(int)
    df.Day = df.Day.astype("int")
    df.Year = df.Year.map(int)
    df.Weekday = df.Weekday.astype("object")
    df = df.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return df



def split_date_continues():
    df = cyclists()
    df2 = split_date(df)
    df = df.drop("Päivämäärä", axis = 1)
    return pd.concat([df2,df], axis = 1)

def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()
