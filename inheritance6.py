# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 13:02:16 2019

@author: Manas
"""

class student():
    def __init__(self):
        self.name=input("enter name of the student ")
        self.roll=input("enter the roll number of student ")
        self.age=input("enter your age ")
class mentors(student):
    def __init__(self):
        super().__init__()
        self.course=input("enter your course name ")
        self.batch=input("enter your batch details ")
    def display(self):
        print("student details are: ")
        print("name\t roll\t age\t course\t\t batch")
        print(self.name,"\t",self.roll,"\t",self.age,"\t",self.course,"\t",self.batch)
m1=mentors()
m1.display()
        