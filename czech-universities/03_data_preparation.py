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

	#Drop (delete) rows with missing values
	df = df.dropna()
	print(df)

#Remove duplicates
df = df.drop_duplicates()
print(df)

#Identify and handle outliers
numerical_cols_dict = {k: v for k, v in dtype_dict.items() if v != np.dtype('O')}
numerical_cols_list = list(numerical_cols_dict.keys())
df_numerical = df[numerical_cols_list]
print(df_numerical)

def handle_outliers(data):
	df_cols = data.columns
	
	for col in df_cols:
		q1 = data[col].quantile(0.25)
		q3 = data[col].quantile(0.75)
		iqr = q3 - q1
		outlier_free_df = df[(df[col] >= (q1 - 1.5 * iqr)) & (df[col] <= (q3 + 1.5 * iqr))]
		data = outlier_free_df
	
	return data

df = handle_outliers(df_numerical)
print(df)
