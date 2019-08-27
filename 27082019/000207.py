# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:00:05 2019

@author: piedi
"""

import numpy as np

#array o fila de 10 ceros
z=np.zeros(10)
print z

#imprime el largo de la fila 
print z.shape 

#cambia la forma del array, de fila a columna de 10 ceros
z.shape=(10,1)

print z