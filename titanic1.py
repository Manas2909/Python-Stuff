# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:07:38 2019

@author: Manas
"""
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import warnings
warnings.filterwarnings('ignore')
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
#from sklearn.metrics import LabelEncoder
print(os.getcwd())
os.chdir("C:\Class Pyhton\datasets")
data=pd.read_csv("titanic-train.csv")
'''
print(os.getcwd())
location=r"C:\Class Pyhton\datasets\titanic-train.csv"
df_train=pd.read_csv(location)
'''
print(data.shape)
print(data.info())
print(data.sort_values(['Fare','Pclass']))
#filtering rows
print(data[data['PassengerId']<=10])
print(data.iloc[3:5])
print(data.isnull().sum())
#data.dropna(inplace=True)
print(data.shape)
#print(data[(data['Age'].mean())].tail())
#print(data['Age'].mean())
#data1=data['Age'].mean()
#print(data['Age'].replace(np.NaN,data1))

'''
#print(data.sample(5))
#print(data.Survived.value_counts())
#print(data.Embarked.value_counts())
#print(data.isnull().sum())
data=data.drop(['PassengerId','Name','Ticket','Cabin'],axis=1)
#print(data.head())
#print(data.groupby(['Pclass']).mean())

def age_approx(cols):
    Age=cols[0]
    Pclass=cols[1]
    if pd.isnull(Age):
        if Pclass==1:
            return 37
        elif Pclass==2:
            return 29
        elif Pclass==3:
            return 25
        else:
            return 24
    else:
        return Age
    
data['Age']=data[['Age','Pclass']].apply(age_approx,axis=1)
print(data.isnull().sum())
data.dropna(inplace=True)
print(data.isnull().sum())
#print(data.dtypes)
#print(data.head())
data_dummy=pd.get_dummies(data,columns=['Sex'])
print(data_dummy.head())
data_dummy=pd.get_dummies(data_dummy,columns=['Embarked'])
print(data_dummy.head())
used_features=["Pclass","Age","SibSp","Parch","Sex_female","Sex_male","Embarked_C","Embarked_Q","Embarked_S"]
X=data_dummy[used_features].values
y=data_dummy['Survived']
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=11,test_size=0.3)
LogReg=LogisticRegression()
LogReg.fit(X_train,y_train)
y_pred=LogReg.predict(X_test)
print(y_pred)
conf_mat=metrics.confusion_matrix(y_test,y_pred)
print("\n",conf_mat)
acc_score=metrics.accuracy_score(y_test,y_pred)
print("\n",acc_score)
print(classification_report(y_test,y_pred))
print(LogReg.coef_)
print(LogReg.intercept_)
print(LogReg.predict_proba(X_test))
'''
