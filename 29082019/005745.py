# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:46:50 2019

@author: piedi
"""

import numpy as np

a=np.array([3,-1,-2,4,-6,8])

#imprime True o False
print a<0

negativos=a<0 
#imprime los negativos
print a[negativos]
print a[a<0]

a[a<0]=0
print a

#si hay por lo menos un numero menos a 8 imprime true 
print (a<8).any()
