# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:05:13 2019

@author: Manas
"""

#Preprocessing
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
'''
x=np.array([[1,3],[4,9],[3,100]])
print(x)
print("mean is:",x.mean())
print("variance is:",x.var())
std=np.sqrt(x.var())
print(std)
x_df=pd.DataFrame(x)
print(x_df)
'''
import seaborn as sns
#sns.distplot(x_df[1],color='green')
#print(x_df[1].plot(kind='hist'))
from sklearn import preprocessing
'''
x_scaled=preprocessing.scale(x_df)
print(x_scaled.mean(),x_scaled.var())
x_prep_df=pd.DataFrame(x_scaled)
print(x_prep_df)
sns.distplot(x_prep_df[1],color='green')
scaler=preprocessing.StandardScaler()
print(scaler.with_mean)
print(scaler.with_std)
ss=scaler.fit_transform(x)
print(ss)
'''
'''
from sklearn.preprocessing import Imputer
data=pd.DataFrame([[2,],[np.nan,0],[1,],[1,1],[np.nan,2]])
print(data)
imputer=Imputer(axis=0,strategy='most_frequent')
print(imputer.fit(data))
print(imputer.transform(data))
'''
from sklearn.preprocessing import MinMaxScaler,MaxAbsScaler
data=[[-1,2],[-0.5,6],[1,15],[0,10],[0,18]]
print(data)
data_df=pd.DataFrame(data)
print(data_df)
scaler=MinMaxScaler()
scaler.fit(data)
print(scaler.data_max_)
print(scaler.transform(data))
x=[[1,-1,2],[2,0,0],[0,1,-1]]
x_df=pd.DataFrame(x)
print(x_df)
mas=MaxAbsScaler()
mas.fit(x)
print(mas.transform(x))