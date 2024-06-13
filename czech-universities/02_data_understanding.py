#!/usr/bin/env python3

#Import libraries
import numpy as np
import pandas as pd

#Import data
df = pd.read_csv('data.csv')
print(df)

#Identify categorical and numerical columns in our DataFrame
df_categorical = df.select_dtypes(include='object')
df_numerical = df.select_dtypes(include='number')
