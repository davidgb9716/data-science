#!/usr/bin/env python3

#Import libraries
import numpy as np
import pandas as pd
from scipy.stats import anderson, shapiro
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler

#Import data
df = pd.read_csv('data.csv')
print(df)

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
def handle_outliers(df):
	def replace_outliers(col):
		non_zero_col = col[col != 0]
		if non_zero_col.empty:
			return col
		q1 = non_zero_col.quantile(0.25)
		q3 = non_zero_col.quantile(0.75)
		iqr = q3 - q1
		lower_bound = q1 - 1.5 * iqr
		upper_bound = q3 + 1.5 * iqr
		median = non_zero_col.median()
		
		def replace_value(x):
			if x == 0:
				return x
			elif lower_bound <= x <= upper_bound:
				return x
			else:
				return median
			
		return col.apply(replace_value)
	
	#Apply only to numerical columns
	numerical_cols = df.select_dtypes(include=['number'])
	outlier_free_df = numerical_cols.apply(replace_outliers, axis=0)
	
	#Combine numerical and non-numerical columns
	non_numerical_cols = df.select_dtypes(exclude=['number'])
	result_df = pd.concat([outlier_free_df, non_numerical_cols], axis=1)
	
	return result_df

df = handle_outliers(df)

df = df.dropna()
df = df.reset_index(drop=True)

print(df)

categorical_columns = df.select_dtypes(include='object').columns

#Handle inconsistent data (standardize data formats)
for col in categorical_columns:
	df[col] = df[col].str.lower()

#Remove Czech columns
df = df.drop(labels=['college_cs', 'faculty_cs', 'study_program_cs'], axis=1)
print(df)

#Save Processed DataFrame
df.to_csv(path_or_buf='processed_dataset.csv', sep=',')
