# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:02:21 2019

@author: Manas
"""
import re
'''

p = re.compile('[a-zA-Z0-9]')
#q = re.compile('[A-Z]')
#r = re.compile('[0-9]')
print(p.findall("Aye, said Mr. Gibenson Stark at 10:00 p.m."))
#print(q.findall("Aye, said Mr. Gibenson Stark at 10:00 p.m."))
#print(r.findall("Aye, said Mr. Gibenson Stark at 10:00 p.m."))  
'''
'''

def text_match(text):
    pattern='ab+'
    if re.search(pattern,text):
        print("pattern found")
    else:
        print("pattern not found")
        
print(text_match("aa"))
'''
'''
def text_match(text):
    pattern='ab?'
    if re.search(pattern,text):
        print("pattern found")
    else:
        print("pattern not found")
        
print(text_match("aa"))
'''
'''
def text_match(text):
    pattern='ab{3}'
    if re.search(pattern,text):
        print("pattern found")
    else:
        print("pattern not found")
        
print(text_match("abbbbc"))
'''
'''
def text_match(text):
    pattern='ab{3,4}'
    if re.search(pattern,text):
        print("pattern found")
    else:
        print("pattern not found")
        
print(text_match("abbbbc"))
'''
'''
def text_match(text):
    pattern='^[a-z]+_[a-z]+$'
    if re.search(pattern,text):
        print("pattern found")
    else:
        print("pattern not found")
        
print(text_match("abb_bbcd"))
'''
'''
def text_match(text):
    pattern='^[a-z]+_[a-z]+$'
    if not re.search(pattern,text):
        print("pattern found")
    else:
        print("pattern not found")
        
print(text_match("abb_bBbcd"))
'''
'''
def text_match(text):
    pattern='a.*b'
    if re.search(pattern,text):
        print("pattern found")
    else:
        print("pattern not found")
        
print(text_match("abbbbcdb"))
'''
'''
def text_match(text):
    pattern='^manas.*'
    if re.search(pattern,text):
        print("pattern found")
    else:
        print("pattern not found")
        
print(text_match("manas kumar"))
'''
'''
def text_match(text):
    pattern='.*manas$'
    if re.search(pattern,text):
        print("pattern found")
    else:
        print("pattern not found")
        
print(text_match("abb_bbcdmanas"))
'''