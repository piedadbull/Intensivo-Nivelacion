# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:26:16 2019

@author: piedi
"""

import numpy as np

#matriz a es de tipo float64
a=np.array([1,2,3,4.0])
#matriz a es de tipo float64, pero le impongo que sea de tipo int32
b=np.array([1,2,3,4.0], dtype='int32')


print a.dtype

print b.dtype