# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 14:06:32 2019

@author: Manas
"""

import numpy as np

def sigmoid(input):
    sigmoid_scores=1/float(1+np.exp(-input))
    return sigmoid_scores
inputs=np.array([-600000,-500000,-2,-3,-5,-6,0,0.00001,0.01,0.1,0.5,1,10,60,600000])
for inp in inputs:
    print(inp,":",sigmoid(inp))
    