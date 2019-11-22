# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 13:06:24 2019

@author: Manas
"""

class decoratorexample:
    def __init__(self):
        print("hello world")
    @classmethod
    def example_classmethod(cls):
        print("class method")
        cls.example_decorator()
    @staticmethod
    def example_decorator():
        print("decorator method")
de = decoratorexample()
de.example_classmethod()