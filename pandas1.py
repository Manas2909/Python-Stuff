# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:42:53 2019

@author: Manas
"""

import pandas as pd
'''
data=[[1,2,2],[3,3,4]]
snd=pd.Series(data)
print(snd)
'''
'''
data=[1,2,3,4,5]
a=pd.DataFrame(data)
print(a)
print(a[0][0])
'''

dict1={'a':1,'b':2,'c':3,'g':7}
dict2={'a':4,'b':5,'c':6,'h':8}
data={'first':dict1,'second':dict2}
df=pd.DataFrame(data)
#print(df)
ac=df.fillna("100")
#print(ac)
#print(df["second"])
#print(type(ac))
#print(type(df[["first","second"]]))
#ad=ac.drop("first",axis=1,inplace=True)
#print(ad)
print(ac)
#print(df.loc["a","first"])
#print(df.iloc[0:4,0:1])
#ad=ac[["first","second"]]>0
ac.reset_index(inplace=True)
print(ac)
ac.set_index('index',inplace=True)
print(ac)
