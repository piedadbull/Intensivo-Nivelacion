# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:24:02 2019

@author: piedi
"""

import numpy as np

a=np.arange(25.0).reshape(5,5)
print a
print ' ' 
#imprime los numeros divisibles por 3 de la matriz a 
print a[a%3==0]
print ' '   

output=np.empty_like(a)
output.fill(np.nan)
#print output

#si el elemento de la matriz a es divisible por 0, pone en numero en la matriz output
mask = a%3 == 0
output[mask]=a[mask]

print output
print ' '  
#donde el elemento de la matriz sea divisible por cero, pone el elemento de dicha matriz, si no pone nan
print np.where(a%3==0,a,np.nan)