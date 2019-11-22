# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:24:07 2019

@author: Manas
"""

import os
import pandas as pd
print(os.getcwd())
os.chdir("D:\\ongoing")
print(os.getcwd())
data=pd.read_csv("50-Startups.csv")
print(data)
print(data.head(3),"\n")
print(data.tail(3),"\n")
print(data.mean,"\n")
print(data['Marketing Spend'].mean(),"\n")
print(data.describe(),"\n")
print(data.head(),"\n")#defaults to 5
print(data.tail(),"\n")

print(data.info(),"\n")
print(data["Profit"],"\n")
