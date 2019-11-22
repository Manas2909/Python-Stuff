# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:35:36 2019

@author: Manas
"""

import os
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
sns.set(style="white",color_codes=True)
sns.set(font_scale=1.5)
print(os.getcwd())
os.chdir("C:\Class Pyhton\datasets")
data=pd.read_csv("Advertising.csv")
print(data)
print(data.shape)
print(data.describe())
print(type(data))
#sns.pairplot(data,x_vars=['TV','radio','newspaper'],y_vars='sales',height=5,aspect=0.9,kind='reg')
feature_cols=['TV','newspaper','radio']
X=data[feature_cols]
y=data['sales']
print(type(y))
#sns.pairplot(X);
print(data.corr())
#sns.heatmap(data,annot=True)
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=1,test_size=0.3)
print(type(X_train))
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
Linreg=LinearRegression()
Linreg.fit(X_train,y_train)
#print(Linreg.intercept_)
#print(Linreg.coef_)
#y=b0+b1x1+b2x2+b3x3
y_pred=Linreg.predict(X_test)
print(y_pred)
print(y_test)
sqrt=np.sqrt(metrics.mean_squared_error(y_test,y_pred))
print("mean abs error mae: ",metrics.mean_absolute_error(y_test,y_pred))
print("mean sq error mse: ",metrics.mean_squared_error(y_test,y_pred))
print("root mean abs error rmse: ",sqrt)
print("r2 value: ",metrics.r2_score(y_test,y_pred))

