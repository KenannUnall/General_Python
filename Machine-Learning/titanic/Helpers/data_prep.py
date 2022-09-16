#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

from sklearn.preprocessing import LabelEncoder

def outlier_thresholds(dataframe, col_name, q1=0.05, q3=0.95):
    q1 = dataframe[col_name].quantile(q1)  # 1.Çeyrek
    q3 = dataframe[col_name].quantile(q3)  # 3.Çeyrek
    interquantile_range = q3 - q1  # range'i hesaplayalım
    low_limit = q1 - 1.5 * interquantile_range # low & up limit:
    up_limit = q3 + 1.5 * interquantile_range
    return low_limit, up_limit

# Outlier Değer Var mı Yok Mu:
def check_outlier(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    if dataframe[(dataframe[col_name] > up_limit) | (dataframe[col_name] < low_limit)].any(axis=None):
        return True
    else:
        return False

# Outlier Değerlere Erişmek:
def grab_outliers(dataframe, col_name, index=False):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    if dataframe[(dataframe[col_name] < low_limit) | (dataframe[col_name] > up_limit)].shape[0] > 10:
        return dataframe[(dataframe[col_name] < low_limit) | (dataframe[col_name] > up_limit)].head()
    else:
        return dataframe[(dataframe[col_name] < low_limit) | (dataframe[col_name] > up_limit)]
    if index:
        outlier_index = dataframe[(dataframe[col_name] < low_limit) | (dataframe[col_name] > up_limit)].index
        return outlier_index

# Outlier Değer Problemini Çözme:

# Silme ile remove_outlierçözümleme:
def remove_outlier (dataframe, col_name, q1=0.05, q3=0.95):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name, q1, q3)
    df_without_outliers = dataframe[~((dataframe[col_name] < low_limit) | (dataframe[col_name] > up_limit))]
    return df_without_outliers

# Baskılama yöntemi:
def replace_with_thresholds(dataframe, variable, q1=0.01, q3=0.99):
    low_limit, up_limit = outlier_thresholds(dataframe, variable, q1, q3)
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    return dataframe

def one_hot_encoder(dataframe, ohe_col_names, drop_first=True):
    dms = pd.get_dummies(dataframe[ohe_col_names], drop_first=drop_first)    # dummy değişken üretilecek kategorik değişkenler (ohe cols)
    df_ = dataframe.drop(columns=ohe_col_names, axis=1)              # dummy değişkene çevirdiğimiz değişkeni dışarıda tutacak yeni df'i oluşturalım
    dataframe = pd.concat([df_, dms],axis=1)                      # 1.ve 2.adımdaki dataframe'i birleştirelim
    return dataframe

def label_encoder(dataframe, binary_col):
    labelencoder = LabelEncoder()
    dataframe[binary_col] = labelencoder.fit_transform(dataframe[binary_col])
    return dataframe