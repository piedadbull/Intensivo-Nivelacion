# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:39:38 2019

@author: piedi
"""

import numpy as np

a=np.array([3,-1,-2,4,-6,8])

#si hay por lo menos un numero menos a 8 imprime true 
print (a<8).any()

#binarios; y, o, no: &,|,
print (a>3) & (a<8)

#imprime lugar de la matriz donde se encuentran los numeros negativos
print np.nonzero(a<0)
