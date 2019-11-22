# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:27:08 2019

@author: Manas
"""

class a():
    def method_A(self):
        print("class a")
class b(a):
    def methodB(self):
        print("class b")

b1=b()
b1.methodB()
b1.method_A()
