#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


# In[10]:


#DATAFRAME İNCELEME METHODU
def info(df):
    print(df.info())
    
def head(df,headdd=5):
    print(df.head(headdd))

def tail(df,taiil=5):
    print(df.tail(taiil))
    
def describe(df):
    print(df.describe())

def describeT(df):
    print(df.describe().T)

def shape(df):
    print(df.shape)

def columns(df):
    print(df.columns)

def dtypes(df):
    print(df.dtypes)

def isNullSum(df):
    print(df.isnull().sum())
    
def describe_function(df):
    print(df.describe().T)
    print("Null var mı? ", df.isnull().values.any())
    
#Grafikler
def histogram(df,*args):
    for i in args:
        df[i].hist(grid=True,figsize=(4,4),color="red")
        plt.xlabel(i)
        plt.ylabel("Frekans")
        plt.title("Veri Sıklığı - {}".format(i))
        plt.show()
        
def heatMap(df):
    sns.heatmap(df.corr(method='pearson').drop([], axis=1).drop([], axis=0),annot = True);
    plt.show()

def scatter(df,column1,column2,hue):
    sns.scatterplot(x=df[column1],y=df[column2],hue=df[hue])
    
def box_plot(data,x,y):
    sns.boxplot(x=x, y=y, data=data,palette="Accent")
    
def pairplot(df,hue):
    sns.pairplot(data=df,hue=hue)
# In[4]:

def valueCounts(df,column):
    return df[column].value_counts()
    
def unique(df,column):
    return df[column].unique()

