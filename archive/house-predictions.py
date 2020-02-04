# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:13:45 2019

@author: Jake
"""

#%%Read in the data
import numpy as np
import pandas as pd

df = pd.read_csv(r"~Jake\Documents\Projects\Predicting-House-Prices\input\train.csv")

#%%Adjusting features for model
import tensorflow as tf

num_fc = tf.feature_column.numeric_column("YearBuilt")
bucketized_feature_column = tf.feature_column.bucketized_column(
        source_column = num_fc,
        boundaries = [1954, 1973, 2000])

#%%Start with just a few features. Will add in more
num_cols = ['TotalBsmtSF', '1stFlrSF', 'GrLivArea', 'GarageArea', 'YearBuilt']
df_num = df[['SalePrice'] + num_cols]

#%%Split data to test and train
from sklearn.model_selection import train_test_split
X = df_num[num_cols].values
y = df_num['SalePrice'].values
X_train, X_test, y_train, y_test = train_test_split(X, y)

#%%Set up model
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

model = Sequential()
model.add(Dense(12, input_dim=X.shape[1], kernel_initializer='normal', activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))

model.summary()

#%%Compile and fit model
model.compile(loss='mse', optimizer='adam', metrics=['mse','mae'])

history = model.fit(X_train, y_train, epochs=40, batch_size=50,  verbose=1, validation_split=0.2)

#%%View training/validation metrics
import matplotlib.pyplot as plt
def trn_v_val(metric):
    plt.plot(history.history[metric])
    plt.plot(history.history['val_%s' % metric])
    plt.title('model %s' % metric)
    plt.ylabel(metric)
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()

print(history.history.keys())

trn_v_val('loss')
trn_v_val('mean_squared_error')
trn_v_val('mean_absolute_error')

#%%Make presictions on the test set
predictions = model.predict(X_test)
plt.scatter(x=y_test, y=predictions)