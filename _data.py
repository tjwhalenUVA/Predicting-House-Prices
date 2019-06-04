# -*- coding: utf-8 -*-
"""
File containing functions to read in the data
@author: Timothy.Whalen
"""

#%% Import Datasets
import pandas as pd
import os

def get_data():
    train = pd.read_csv(os.path.join(os.getcwd(), 'input\\train.csv'))
    test = pd.read_csv(os.path.join(os.getcwd(), 'input\\test.csv'))
    return(train, test)

#%%Clean up missing values
def fill_missing(df, _null_list):
    for c in _null_list.index:
        if str(df[c].dtype) == 'object':
            df[c] = df[c].fillna('None')
        else:
            df[c] = df.groupby('Neighborhood').transform(lambda x: x.fillna(x.mean()))
    
    return(df)

#%%List of columns by type
def get_col_list(df):
    tc = list(df.columns)
    _cat_col = tc[2:3] + tc[5:17] + tc[21:26] + tc[27:34] + tc[35:36] + tc[39:43] + tc[53:54] + tc[55:56] + tc[57:59] + tc[60:61] + tc[63:66] + tc[72:75] + tc[78:80]
    _num_col = list(set(tc) - set(_cat_col))
    return(_cat_col, _num_col)