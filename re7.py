# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:22:05 2019

@author: Manas
"""

import re 
  
 
print(re.sub('ub', '~*' , 'Subject has Uber booked already', flags = re.IGNORECASE)) 
  

print(re.sub('ub', '~*' , 'Subject has Uber booked already')) 
  

print(re.sub('ub', '~*' , 'Subject has Uber booked already', count=1, flags = re.IGNORECASE)) 
  

print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)) 