# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 18:58:26 2020

@author: Jake
"""
import pandas as pd
import os

#Load the Data
DATA_PATH = os.path.join(os.getcwd(), 'input')

def load_housing_data(data_path = DATA_PATH, read_test=True):
    train = pd.read_csv(os.path.join(data_path, 'train.csv'))
    if read_test:
        test = pd.read_csv(os.path.join(data_path, 'test.csv'))
    return(train, test)