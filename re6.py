# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:20:16 2019

@author: Manas
"""

import re 
   
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1)) 
  
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags = re.IGNORECASE)) 
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here')) 