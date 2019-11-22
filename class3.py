# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 13:09:28 2019

@author: Manas
"""

class student():
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        
        
    def display(self):
        print("Name of student is",self.name)
        print("Roll NO of student is",self.roll_no)
        print("Marks of student is",self.marks)
name=input("enter your name")
marks=input("enter your marks")
roll=input("enter your roll")
stud1=student(name,roll,marks)
stud1.display()
#stud2=student("mukul",24,79)

#stud2.display()        