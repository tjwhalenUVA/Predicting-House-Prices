# -*- coding: utf-8 -*-
"""
Predicting House Prices (Kaggle)

Created on Wed May 29 12:57:12 2019

@author: Timothy.Whalen
"""
import pandas as pd
from pathlib import Path
import os

#%% Get Data
import _data
train, test = _data.get_data()

#%% Check for NULL values
_train_null = train.isnull().sum().sort_values(ascending=False)
_train_null = _train_null[_train_null > 0]

_test_null = test.isnull().sum().sort_values(ascending=False)
_test_null  = _test_null [_test_null  > 0]

#Fill Some of the values
train = _data.fill_missing(train, _train_null)
test = _data.fill_missing(test, _test_null)

#%% Create Dummy Variables
tc = train.columns.tolist() #list of column names
#Column names that need to be turned into dummies
cat_columns = [tc[2]] + tc[5:17] + tc[21:26] + tc[27:34] + [tc[35]] + tc[39:43] + [tc[53]] + [tc[55]] + tc[57:59] + [tc[60]] + tc[63:66] + tc[72:75] + tc[78:80]
#Create the dummies and drop the first created column
train = pd.get_dummies(train, columns = cat_columns, drop_first=True)
test = pd.get_dummies(test, columns = cat_columns, drop_first=True)

#%%Tain Model
X_train = train.drop(['Id', 'SalePrice'], axis=1)
y_train = train[['SalePrice']]

# Get missing columns in the training test
missing_cols = set( train.columns ) - set( test.columns )
# Add a missing column in test set with default value equal to 0
for c in missing_cols:
    test[c] = 0
# Ensure the order of column in the test set is in the same order than in train set
test = test[train.columns]

X_test = test.drop(['Id', 'SalePrice'], axis=1)

#%% Set up model
from sklearn.linear_model import LinearRegression
reg = LinearRegression().fit(X_train, y_train)
reg.score(X_train, y_train)
reg.coef_
reg.intercept_

y_test = reg.predict(X_test).flatten() * -1

#Results DF
price_predict = pd.DataFrame({'Id': test.Id.tolist(), 'SalePrice': y_test})

_result_file = Path(os.getcwd()) / "results/predictions.csv"

price_predict.to_csv(str(_result_file), index=False)
