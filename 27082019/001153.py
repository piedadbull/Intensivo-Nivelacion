# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:26:57 2019

@author: piedi
"""

import numpy as np 
from skimage import io
import matplotlib.pyplot as plt

a=np.array([1,2,3,4,5])
b=np.array([7,8,3,1,3])
#multiplicamos las dos matrices 
print a*b
#sumamos las dos matrices
print a+b

#ordena la matriz b de menos a mayor
c=np.sort(b)
print c