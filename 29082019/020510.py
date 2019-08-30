# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 21:02:20 2019

@author: piedi
"""

import numpy as np

a=np.array([[1,2,3],[4,5,6]])

#suma los elementos de la matriz
print a.sum()
print ' ' 
#suma por columna 1+4, 2+5
print a.sum(axis=0)
#print a.sum(axis=-2) es lo mismo que el de arriba 
print ' ' 
#suma por fila 1+2+3 , 4+5+6
print a.sum(axis=-1)
#print a.sum(axis=1) es lo mismo que el de arriba