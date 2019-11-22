# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:24:36 2019

@author: Manas
"""

#linear regeration
from sklearn import linear_model
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
height=[[4.0],[4.5],[5.0],[5.2],[5.4],[5.8],[6.1],[6.2],[6.4],[6.8]]
weight=[42,44,49,55,53,58,60,64,66,69]
#print("height weight")
reg=linear_model.LinearRegression(n_jobs=2)
reg.fit(height,weight)
print(reg.predict([[3.0]]))

