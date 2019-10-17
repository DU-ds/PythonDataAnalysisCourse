#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:27:57 2019

@author: du_ds
"""



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

