# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:40:30 2019

@author: Timothy.Whalen
"""
#%% Import user modules
import _dataImport

#%% Import libraries for remaing analysis

#%% Get the data
train, test = _dataImport.get_data()

#%% Missing Values
#Find the % of records for a variable missing data
_null = train.isnull().sum().sort_values(ascending=False)  / train.shape[0]
#Plot shows the features missing more than 10% of records
_null[_null > 0.1].plot('barh')

#PoolQC
train['PoolQC'].unique() #4 levels, one is nan, fill with 'None'

#MiscFeature
train['MiscFeature'].unique() #5 levels, one is nan, fill with 'None'

#Alley

#Fence

#FireplaceQu

#LotFrontage
