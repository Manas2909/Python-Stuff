# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:31:44 2019

@author: Manas
"""

import os
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import seaborn as sns
import graphviz
from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestRegressor

print(os.getcwd())
os.chdir("C:\\Class Pyhton\\datasets")
data=pd.read_csv("temps.csv")
print(data)
print(data.shape)
print(data.describe())
data_dummy=pd.get_dummies(data,columns=['week'])
print(data_dummy)
y=data_dummy['actual']
data=data_dummy.drop('actual',axis=1)
feature_list=data_dummy.columns
X=data_dummy[feature_list]
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=2,test_size=0.3)
'''
dtr=DecisionTreeRegressor(criterion='mse',min_samples_leaf=10,max_depth=4)
dtr.fit(X_train,y_train)
y_pred = dtr.predict(X_test)
print(y_pred)
print(dtr.score(X_test,y_test))
#print(accuracy_score(y_test,y_pred))
dot_data=export_graphviz(dtr,out_file=None,feature_names= feature_list,class_names=data_dummy['actual'].unique(),filled=True,rounded=True,special_characters=True)
graph= graphviz.Source(dot_data)
graph.render("C:\\Class Pyhton\\temps_graph4")
'''
rf=RandomForestRegressor(n_estimators=1000,random_state=42)
rf.fit(X_train,y_train)
y_pred = rf.predict(X_test)
print(y_pred)
errors=abs(y_pred-y_test)
print(errors)
print(errors)
tree=rf.estimators_[5]
dot_data=export_graphviz(tree,out_file=None,feature_names= feature_list,
                         #class_names=data_dummy['actual'].unique(),
                         filled=True,rounded=True,special_characters=True)
graph= graphviz.Source(dot_data)
graph.render("C:\\Class Pyhton\\temps_random_forest2")
importances=list(rf.feature_importances_)
print(importances)
print("##############################")
print(list(zip( feature_list, importances)))
print("---------------------------------")
feature_importance=[(feature,round(importance ,2)) for feature,importance in zip(feature_list,importances)]
print(feature_importance)
print(111111111111111111111111111111)
feature_importance=sorted(feature_importance,key=lambda x:x[1], reverse=True)
print(feature_importance)
