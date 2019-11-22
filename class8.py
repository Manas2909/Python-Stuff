# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:10:02 2019

@author: Manas
"""

class demo():
    n=0
    def __init__(self):
        demo.n+=1
    @staticmethod
    def num_of_objects():
        print("number of objects are: ",demo.n)
d1=demo()
d2=demo()
d2.num_of_objects()
