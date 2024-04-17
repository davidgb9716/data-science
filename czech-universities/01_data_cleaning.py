#!/usr/bin/env python3

#Import libraries
import numpy as np
import pandas as pd

#Import data
df = pd.read_csv('data.csv')
print(df)

#Define the column's data types
dtype_dict = {col: dtype for col, dtype in zip(df.columns, df.dtypes)}
print(dtype_dict)

#Identify missing values
missing_values = df.isna() #Using isna() over isnull() is recommended as a best practice.
print(missing_values.sum())
