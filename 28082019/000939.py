# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:05:48 2019

@author: piedi
"""

import numpy as np

b=np.array([(1.5,2,3,),(4,5,6)])
#imprime una matriz bodimensional 
print b

lista2=[[1,2,3,4,5],[6,7,8,9,10]]
#matriz de dos dimensiones a partir de 2 listas
x=np.array([lista2])
print'-----------'
print x

#matriz de 3,4 (filas, columnas) de puros ceros 
a=np.zeros((3,4))
print a