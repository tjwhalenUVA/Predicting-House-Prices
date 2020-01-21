# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:40:30 2019

@author: Timothy.Whalen
"""
#%% Import user modules
import _data

#%% Import libraries for remaing analysis
import pandas as pd

#%% Get the data
train, test = _data.get_data()

#%% Missing Values
#Find the % of records for a variable missing data
_null = train.isnull().sum().sort_values(ascending=False)  / train.shape[0]
#Plot shows the features missing more than 10% of records
_null[_null > 0.1].plot('barh')

#PoolQC
train['PoolQC'].unique() #4 levels, one is nan, fill with 'None'
train['PoolQC'] = train.PoolQC.fillna('None')

#MiscFeature
train['MiscFeature'].unique() #5 levels, one is nan, fill with 'None'
train['MiscFeature'] = train.MiscFeature.fillna('None')

#Alley
train['Alley'].unique() #3 levels, one is nan, fill with 'None'
train['Alley'] = train.Alley.fillna('None')

#Fence
train['Fence'].unique() #5 levels, one is nan, fill with 'None'
train['Fence'] = train.Fence.fillna('None')

#FireplaceQu
train['FireplaceQu'].unique() #5 levels, one is nan, fill with 'None'
train['FireplaceQu'] = train.FireplaceQu.fillna('None')

#LotFrontage
train['LotFrontage'].unique() #Continuous variable, look to fill with an average
#Code below fills NAN values in LF with grouped values by neighborhood
train['LotFrontage'] = train.groupby('Neighborhood').transform(lambda x: x.fillna(x.mean()))

#%% Finding correlated values to Sales Price
_cat_c, _num_c = _data.get_col_list(train)
#Calc corr to SalesPrice on all columns
_corr = train[_num_c].corr()[['SalePrice']].reset_index().sort_values('SalePrice', ascending=False)

