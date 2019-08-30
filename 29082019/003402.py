# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:34:03 2019

@author: piedi
"""

import numpy as np

c=np.array([[10,11,12],[20,21,22]])

print c.ndim
#imprime el 0,0 (10) de la matriz bidimencional c
print c[0,0]

a= c=np.array([10,11,12,13,14])

#imprime desde el 1 AL 2 (11 y 12), el ultimo termino no se incluye
print a[1:3]
#imprime desde el 1 AL -2 (11,12,13)
print a[1:-1]

print a[-4:3]


#imprime los primeros tres elementos de la matriz a, es lo mismo que decir a[0:3]
print a[:3]

#imprime desde el -2 hasta el ultimo elemento
print a[-2:]

#desde el principio hasta el final, pero cada dos elementos
print a[::2]