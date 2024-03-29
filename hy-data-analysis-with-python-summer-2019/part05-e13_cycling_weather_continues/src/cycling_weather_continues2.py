#!/usr/bin/env python3

import os
from sklearn.linear_model import LinearRegression   
import pandas as pd


def cyclists(f):
    df = pd.read_csv(f, sep = ";")
    df = df.dropna(axis = 0, how = "all")
    return df.dropna(axis = 1, how = "all")

def split_date(df):
    df = df.iloc[:,0].str.split(expand = True)
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


def split_date_continues(f):
    df = cyclists(f)
    df2 = split_date(df)
    df = df.drop("Päivämäärä", axis = 1)
    return pd.concat([df2,df], axis = 1)

def cyclists_per_day():
    f = os.path.dirname(os.path.realpath(__file__)) + "/Helsingin_pyorailijamaarat.csv"
    df = split_date_continues(f)
    df = df.drop(["Hour","Weekday"], axis = 1)
    groups = df.groupby(["Year", "Month", "Day"])
    return groups.sum()


def cycling_weather():
    f1 = os.path.dirname(os.path.realpath(__file__)) + "/Helsingin_pyorailijamaarat.csv"
    df_cycles = split_date_continues(f1)
    f2 = os.path.dirname(os.path.realpath(__file__)) + "/kumpula-weather-2017.csv"
    df_weather = pd.read_csv(f2)
    left_keys = ['Day', 'Month', 'Year'] 
    right_keys = ['d', 'm', 'Year']
    df = pd.merge(df_cycles, df_weather, left_on = left_keys, right_on = right_keys)
    return df
# .drop(["m", "d", "Time", "Time zone"], axis = 1)
    
# how about I do an outer join, then leave the day month year info alone,
# then group by day, sum over it, then get daily counts?
# not an outer join. a many to one (inner) join

# (df_cycles.Year == 2017).sum()
# Out[19]: 8760
#cycling_weather_df.shape[0]
#Out[21]: 8760    
# so cycling_weather is close to correct. 

def cycling_weather_continues(station):
    cyclists = cyclists_per_day()
    daily_counts = cyclists.sum(axis = 1)
    daily_2017 = daily_counts[1096:1461]
    # aug_2017 = daily_counts[1308:1339] 
    # adjust to take 2017 instead of august 2017
    pd.merge(daily_2017, df_weather)
    # fill in values with forward fill:
    # https://stackoverflow.com/questions/41589365/filling-missing-values-using-forward-and-backward-fill-in-pandas-dataframe-ffil#41589383

    # then use station as dv in a linear regression
    # explanatory variables:
    # 'Precipitation amount (mm)', 'Snow depth (cm)', and 'Air temperature (degC)'
    # fit an intercept
    
    # return tuple: ((*coefs), score)
    
    return ((0.0, 0.0, 0.0), 0.0)
    
def main():
    return

if __name__ == "__main__":
    main()
