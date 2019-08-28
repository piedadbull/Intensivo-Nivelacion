# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:21:16 2019

@author: piedi
"""

import numpy as np
#matriz con numeros al azar entre 0-1
a=np.random.randint(1,10,6)
a=a.reshape(3,2)
#suma los numeros de la fila
b=a.sum(axis=1)
#suma los numeros d elas columas
c=a.sum(axis=0)
print a
print b
print c

