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