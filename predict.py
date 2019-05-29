# -*- coding: utf-8 -*-
"""
Predicting House Prices (Kaggle)

Created on Wed May 29 12:57:12 2019

@author: Timothy.Whalen
"""

#%% Import Datasets
import pandas as pd
import os
train = pd.read_csv(os.path.join(os.getcwd(), 'input\\train.csv'))
test = pd.read_csv(os.path.join(os.getcwd(), 'input\\test.csv'))

#%% Variables missing a lot of data
#Find the % of records for a variable missing data
#_null = train.isnull().sum().sort_values(ascending=False)  / train.shape[0]
#_null_col = _null[_null > 0]#.index.to_list() #columns mising more then 40%


#%% Create Dummy Variables
tc = train.columns.to_list() #list of column names
#Column names that need to be turned into dummies
cat_columns = [tc[2]] + tc[5:17] + tc[21:26] + tc[27:34] + [tc[35]] + tc[39:43] + [tc[53]] + [tc[55]] + tc[57:59] + [tc[60]] + tc[63:66] + tc[72:75] + tc[78:80]
#Create the dummies and drop the first created column
train = pd.get_dummies(train, columns = cat_columns, drop_first=True)
test = pd.get_dummies(test, columns = cat_columns, drop_first=True)



