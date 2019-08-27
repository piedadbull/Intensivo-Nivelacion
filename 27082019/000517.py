# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:33:09 2019

@author: piedi
"""

import numpy as np 

#matriz de 6 numeros aleatorios del 0 al 9
z=np.random.randint(10,size=6)

print z
#imprime el primer elemento de la matriz 
print z[0]
#imprime desde el primer elemento de la matriz hasta el segundo
print z[0:2]
#imprime el ultimo elemento de la matriz
print z[-1]