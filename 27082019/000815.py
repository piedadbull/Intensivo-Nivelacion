# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:05:24 2019

@author: piedi
"""

import numpy as np 
from skimage import io
import matplotlib.pyplot as plt

foto=io.imread('foto.png')
#type(foto)
#matriz de la foto
print foto.shape
#imprime la foto
plt.imshow(foto)

#calcular el seno de todos los numeros en la matriz
foto_sin=np.sin(foto)
print foto_sin

#suma todos los numeros de la matriz 
print(np.sum(foto))
#multiplica todos los numeros de la matriz 
print(np.prod(foto))
#el max de todos los numeros de la matriz 
print(np.max(foto))

