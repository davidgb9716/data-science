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
