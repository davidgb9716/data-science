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

#Handle missing values (by imputation or deletion)
missing_values_list = list(missing_values.sum())

if sum(missing_values_list) != 0:
	#Impute cells with missing values
	df = df.fillna(df.mean())
	print(df)

	#Drop rows with missing values
	df = df.dropna()
	print(df)
