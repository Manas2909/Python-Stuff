# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:40:30 2019

@author: Manas
"""

class A():
    def __init__(self):
        print("class A init")
    
class B(A):
     def __init__(self):
        print("class B init")
    
b1=B()
