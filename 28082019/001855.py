# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:35:04 2019

@author: piedi
"""

import numpy as np

a=np.arange(10)
print a

#ordena de forma aleatoria los numeros de la matriz a creada anteriormente
np.random.shuffle(a)
print a

#elige un numero de forma aleatoria de la matriz a
print np.random.choice(a)
