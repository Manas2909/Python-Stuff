# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:53:12 2019

@author: Manas
"""

import os
import numpy as np
import pandas as pd
print(os.getcwd())
os.chdir("C:\Class Pyhton\datasets")
data=pd.read_csv("titanic-train.csv")
print(data)
print(data.Sex.value_counts())
print(data.isnull().sum())