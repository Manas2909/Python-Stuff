# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:24:18 2019

@author: Manas
"""

import os
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
#%matplotlib inline
sns.set(style="white",color_codes=True)
sns.set(font_scale=1.5)
print(os.getcwd())
os.chdir("C:\Class Pyhton\datasets")
data=pd.read_csv("glass.csv")
print(data)
#sns.lmplot(x='Al',y='RI',data=data)
feature_cols=['Al','Si','K']
X=data[feature_cols]
y=data['RI']
Linreg=LinearRegression()
Linreg.fit(X,y)
data["RI_pred"]=Linreg.predict(X)
print(data)
#sns.lmplot(x='K',y='RI_pred',data=data)
print(Linreg.intercept_ + Linreg.coef_*2)
print(Linreg.predict([[2,3,4],[1,2,1]]))
print(data.Type.value_counts().sort_index())
data['household']=data.Type.map({1:0,2:0,3:0,5:1,6:1,7:1})
print(data)
print(data.household.value_counts())
'''
plt.scatter(data.Al,data.household)
plt.xlabel("Al")
plt.ylabel("household")
sns.lmplot(x='Al',y='household',data=data)

'''
linreg=LinearRegression()
feature=['Al']
M=data[feature]
n=data.household
linreg.fit(M,n)
data['household_pred']=linreg.predict(M)
print(data)
data['household_pred_class']=np.where(data.household_pred>=0.5,1,0)
print(data)
logreg=LogisticRegression()
cols=['Al']
O=data[cols]
p=data.household
logreg.fit(O,p)
data['household_pred_class']=logreg.predict(O)
print(data)
data['household_pred_prob']=logreg.predict_proba(O)[:,1]
print(data)
plt.scatter(data.Al,data.household)
plt.xlabel("Al")
plt.ylabel("household")
plt.plot(data.Al,data.household_pred_prob,color='red')
