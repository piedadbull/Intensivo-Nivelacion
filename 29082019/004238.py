# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:36:11 2019

@author: piedi
"""

import numpy as np

a=np.arange(25).reshape(5,5)

print a

print 'columnas 1 y 3; rojo'
print a[:,1::2]
print ' ' 

print 'ultima fila; amarillo'
print a[4,:]
print ' ' 

print 'el 5,7,15 y 17'
print a[1::2,0:3:2]