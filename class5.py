# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 12:43:01 2019

@author: Manas
"""

class car():
  
    cost=0
    def __init__(self):
        self.brand_name=input("enter the brand name ")
        self.model_name=input("enter the model name ")
        print()
    def accept(self):
       
        self.cost=input("enter the cost ")
        
    def display(self):
        print("Brand Name of car is",self.brand_name)
        print("Model name of car is",self.model_name)
        print("cost of car is",self.cost)
    
    def modify(self):
        self.cost=input("enter the modified cost ")
        
        
        
car1=car()
car1.accept()
car1.display()
car2=car()
car2.accept()
car2.display()
car2.modify()
print("car 2 details")
car2.display()
print("car 1 details")
car1.display()
