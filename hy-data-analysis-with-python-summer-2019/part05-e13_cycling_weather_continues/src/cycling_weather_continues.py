#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:55:32 2019

"""

import os
from sklearn.linear_model import LinearRegression   
import pandas as pd

def cyclists(f):
    df = pd.read_csv(f, sep = ";")
    df = df.dropna(axis = 0, how = "all")
    return df.dropna(axis = 1, how = "all")

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



def prep_data():
    f1 = "/home/du_ds/Documents/Git/PythonDataAnalysisCourse/hy-data-analysis-with-python-summer-2019/part05-e13_cycling_weather_continues/src/Helsingin_pyorailijamaarat.csv"
    f2 = "/home/du_ds/Documents/Git/PythonDataAnalysisCourse/hy-data-analysis-with-python-summer-2019/part05-e13_cycling_weather_continues/src/kumpula-weather-2017.csv"
#    f1 = os.path.dirname(os.path.realpath(__file__)) + "/Helsingin_pyorailijamaarat.csv"
    df_cycles = split_date_continues(f1)
    t = ['Day', 'Month', 'Year']
    df_cycles = df_cycles.loc[(df_cycles.Year == 2017),:]
    df_cycles = df_cycles.drop(["Hour"], axis = 1)
    df_cycles = df_cycles.groupby(t).sum()
    df_cycles.reset_index(inplace = True)
#    f2 = os.path.dirname(os.path.realpath(__file__)) + "/kumpula-weather-2017.csv"
    df_weather = pd.read_csv(f2)
    cols = dict(zip(['d', 'm'],['Day', 'Month']))
    df_weather = df_weather.rename(columns = cols)
    df_weather = df_weather.drop([ "Time", "Time zone"], axis = 1)
    df = pd.merge(df_cycles, df_weather, on = t)
#df.isnull().sum()
#Snow depth (cm)   7
#the rest are zeros
    df = df.ffill()
    return df
#df2.isnull().sum().sum()
#0


def cycling_weather_continues(station):
    """
    takes a valid measuring point along the bike routes, 
    and models the relationship with the weather (temp(C) precipitation(mm) snow depth(cm))
    using a linear regression model data aggregated and filtered
    so it's one entry for every day of 2017
    """
    
    # prep data
    df = prep_data()
    
    features = df.loc[:,['Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)']]
    response = df.loc[:,station]
    fm = LinearRegression(fit_intercept = True)
    fm.fit(features, response)
    coefs = fm.coef_
    score = fm.score(features, response)
    return ((coefs), score)

"""
Exercise 13 (cycling weather continues)

Write function cycling_weather_continues that tries to explain with 
linear regression the variable of a cycling measuring station’s counts
 using the weather data from corresponding day. The function should 
 take the name of a (cycling) measuring station as a parameter and 
 return the regression coefficients and the score. In more detail:

Read the weather data set from the src folder. Read the cycling data 
set from folder src and restrict it to year 2017. Further, get the 
sums of cycling counts for each day. Merge the two datasets by the 
year, month, and day. Note that for the above you need only small 
additions to the solution of exercise cycling_weather. After this, 
use forward fill to fill the missing values.

In the linear regression use as explanatory variables the following columns 
'Precipitation amount (mm)', 'Snow depth (cm)', and 'Air temperature (degC)'. 
Explain the variable (measuring station), whose name is given as a parameter 
to the function cycling_weather_continues. Fit also the intercept. The 
function should return a pair, whose first element is the regression 
coefficients and the second element is the score. Above, you may need to 
use the method reset_index (its counterpart is the method set_index).

The output from the main function should be in the following form:

Measuring station: x
Regression coefficient for variable 'precipitation': x.x
Regression coefficient for variable 'snow depth': x.x
Regression coefficient for variable 'temperature': x.x
Score: x.xx

Use precision of one decimal for regression coefficients, and precision 
of two decimals for the score. In the main function test you solution 
using some measuring station, for example Baana.

"""

def main():
    station = 'Merikannontie'
    #"Baana"
    coefs, score = cycling_weather_continues(station)
    print("Measuring station: %s" % station)
    print(f"Regression coefficient for variable 'precipitation': %.1f" % coefs[0])
    print(f"Regression coefficient for variable 'snow depth': %.1f" % coefs[1])
    print(f"Regression coefficient for variable 'temperature': %.1f" % coefs[2])
    print(f"Score: %.2f" % score)

if __name__ == "__main__":
    main()