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

#%% Find the % of records for a variable missing data
_null_train = train.isnull().sum().sort_values(ascending=False)  / train.shape[0]
_null_test = test.isnull().sum().sort_values(ascending=False)  / test.shape[0]

#%% Columns that should be removed?
#Plot shows the features missing more than 10% of records
_null_train[_null_train > 0.5].plot('barh')
_null_test[_null_test > 0.5].plot('barh') #Same features missing from test set
#4 features that are null in over 90% of records; drop for now
_null_train[_null_train > 0.5].index
#Drop Fence quality, Alley entrance type, Miscellaneous Features, Pool Quality
train = train.drop(['Fence', 'Alley', 'MiscFeature', 'PoolQC'], axis=1)
test = test.drop(['Fence', 'Alley', 'MiscFeature', 'PoolQC'], axis=1)

#%% Fill Missing Values on Additional Columns
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

