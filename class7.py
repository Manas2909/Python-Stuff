# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 13:23:58 2019

@author: Manas
"""

class sample():
    x=5
    y=10
    @classmethod
    def modifyx(cls):
        cls.x=10
    @classmethod
    def modifyy(cls):
        cls.y=5
s=sample()
s2=sample()
#print(s.x," ",s.y)

#print(s2.x," ",s2.y)
s.modifyx()
s2.modifyy()
print(s.x," ",s.y)
print(s2.x," ",s2.y)