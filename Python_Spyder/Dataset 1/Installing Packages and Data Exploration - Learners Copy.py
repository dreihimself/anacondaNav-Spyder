# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:24:57 2022

@author: Paolo Hilado
"""
#Installing relevant python packages
'''
pip install researchpy
pip install pandas
pip install os
'''

# Activity 1 ------------------------------------------------------
import pandas as pd
import os
import researchpy as rp

#Checking out the current working directory
print(os.getcwd())
#Loading a spreadsheet and assigning it to a variable
#We will open and work on "ExperimentOne.xlsx"
df = pd.read_excel("ExperimentOne.xlsx")
#Viewing the dataframe
df
# Viewing the first rows
df.head(10)
# Viewing the last rows
df.tail(10)

#Slicing the dataframe
df.iloc[:, 1]
df.iloc[:49, [0,1]]
df.iloc[[5,6,50,57], :]

#Checking the structure of the dataframe
df.info()

#Checking for NAs or missing cases
df.isnull().values.any()

#Getting a simple descriptives
df.iloc[:, 1].describe() #works with post test measures

# Activity 2 ------------------------------------------------------
#Checking out the current working directory
print(os.getcwd())
#Loading a spreadsheet and assigning it to a variable
#We will open and work on "ExperimentTwo.xlsx"
df2 = pd.read_excel("ExperimentTwo.xlsx")
#Viewing the dataframe
df2
# Viewing the first 7 rows
df2.head(7)
# Viewing the last 7 rows
df2.tail(7)

#Slicing the dataframe
#Slice the second column with all of its observations
df2.iloc[:, 1]
#Slice the data frame to only include observations ID of 5 to 20
df2.iloc[5:21, :] 
#Slice the data frame to only include column ID and pretest with observation ID 7 to 25
df2.iloc[7:26, :2]
#Checking the structure of the dataframe
df2.info()

#Checking for NAs or missing cases
df2.isnull().values.any()
#Getting a simple descriptives
df2.describe()

# Activity 3 ------------------------------------------------------
# Installing needed dependency
#pip install pyreadstat
#Checking out the current working directory
print(os.getcwd())
#Loading a .Sav file and assigning it to a variable
#We will open and work on "Bank.sav"
df = pd.read_spss("Bank.sav")
#Viewing the dataframe
df
# Viewing the first 15 rows
df.head(15)
# Viewing the last 15 rows
df.tail(15)
#Checking the structure of the dataframe
df.info()
#Slicing the dataframe
#Slice the second column with all of its observations
df.iloc[:, 1]
#Slice the data frame to only include observations index of 30 to 50
df.iloc[30:51, :]
#Slice the data frame to only include column ID with labels 735 and 736
df[(df['id']== 735) | (df['id']== 736)]
#Slice the data frame to only include those with salbeg >10,000 AND age > 30
sub1 = df[(df['salbeg'] > 10000) & (df['age'] > 30)]
sub1
#Slice the data frame to only include those with salbeg >10,000 OR age > 30
sub2 = df[(df['salbeg'] > 10000) | (df['age'] > 30)]
#Rename column 'edlevel' to 'education'
df = df.rename(columns = {'edlevel':'education'})
#Checking for NAs or missing cases
df.isnull().values.any()
#Getting a simple descriptives
desc = df.describe()
desc

# Activity 4 ------------------------------------------------------
#Checking out the current working directory
print(os.getcwd())
#Loading a .Sav file and assigning it to a variable
#We will open and work on "Bank.sav"
df = pd.read_spss("Personality.sav")
#Viewing the dataframe
df
# Viewing the first 5 rows
df.head(5)
# Viewing the last 5 rows
df.tail(5)
#Checking the structure of the dataframe
df.info()
#Slicing the dataframe
#Slice column 3 to 5 with all of its observations
df.iloc[:, 2:5]
#Slice the data frame to only include observations index of 15 to 35
df.iloc[15:35, :]

#Checking for NAs or missing cases
df.isnull().values.any()
#Subset dataframe to include all rows with missing cases
missing_df1= df[df.isnull().all(axis=1)]
missing_df1= df[df.isnull().any(axis=1)]
#Subset dataframe to include all rows with complete cases
complete_df= df[df.notnull().all(axis=1)]
#Getting a simple descriptives
desc = df.describe()
desc
# Activity 5 ------------------------------------------------------
#Loading a .Sav file and assigning it to a variable
#We will open and work on "sales.sav"
df = pd.read_spss("sales.sav")

#Viewing the dataframe
df
# Viewing the first 15 rows
df.head(15)
# Viewing the last 15 rows
df.tail(15)
#Checking the structure of the dataframe
df.info()
#Slicing the dataframe
#Slice column to include 'hiqualty', 'satinfo', 'salesrep' with all of its observations
df.loc[:,['hiqualty', 'satinfo', 'salesrep']]
#Slice the data frame to only include observations index of 15 to 35
df.iloc[15:36, :]
#Change the column named 'hiqualty' to 'hiquality'
df = df.rename(columns={'hiquality':'highquality'})
#Checking for NAs or missing cases
df.isnull().values.any()
#Subset dataframe to include all rows with missing cases
missing_df1= df[df.isnull().all(axis=1)]
missing_df1= df[df.isnull().any(axis=1)]
#Subset dataframe to include all rows with complete cases
complete_df= df[df.notnull().all(axis=1)]
#Getting a simple descriptives
df.describe()

