# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:49:16 2019

@author: Manas
"""

import pandas as pd
import numpy as np
'''
s1=pd.Series([[1,2,3,4],[6,3,5]])
s2=pd.Series([1.1,2.2,3.3,4.4,5.6,7.8,9.2])
s3=pd.Series(['a','b','c','d','e','f'])
data={'first':s1,'second':s2,'third':s3}
dfseries=pd.DataFrame(data)
print(dfseries)
'''
#when data is 2d numpy ndarray, one constraint has to be maintained while creating a datafram of 2d arrays-dimensions od 2d array must be same
'''
d1=[[2,3,4],[5,6,7]]
d2=[[2,4,8],[1,3,9]]
data={'first':d1,'second':d2}
df2d=pd.DataFrame(data)
print(df2d)
'''
#program to create dataframe from 2d array
'''
d1=[[2,3,4],[5,6,7]]
d2=[[2,4,8],[1,3,9]]
data=[d1,d2]
df2d=pd.DataFrame(data)
print(df2d)
'''
'''
dictionary={"country":["brazil","russia","india","china","soth africa"],
            "capital":["brasilia","moscow","new delhi","beijing","pretoria"],
            "area":[8.516,17.10,3.286,9.597,1.221],
            "population":[200.4,143.5,1252,1357,52.98]}
brics=pd.DataFrame(dictionary)
print(brics,"\n")
brics.index=["br","ru","in","ch","sa"]
print(brics,"\n")
print(brics.head(3),"\n")
print(brics.tail(3),"\n")
print(brics.mean,"\n")
print(brics['area'].mean(),"\n")
print(brics.describe(),"\n")
'''
#create date & days

dates_d=pd.date_range('20300101',periods=6,freq='d')
print("days",dates_d)
date_m=pd.date_range('20200101',periods=6,freq='m')
print("month:",date_m)
date_y=pd.date_range('20300101',periods=6,freq='y')
print("year:",date_y)
random=np.random.rand(6,4)
df=pd.DataFrame(random,index=dates_d,columns=list('abcd'))
print(df)