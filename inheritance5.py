# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:48:22 2019

@author: Manas
"""

class A():
    def __init__(self):
        self.x=10
        print("class A init")
    
class B(A):
    def __init__(self):
        super().__init__()
        self.y=20
        print("class B init")
    def display(self):
        print(self.x ,":",self.y)
b1=B()
b1.display()