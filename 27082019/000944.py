# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:16:29 2019

@author: piedi
"""

import numpy as np 
from skimage import io
import matplotlib.pyplot as plt

foto=io.imread('foto.png')
#type(foto)
#matriz de la foto
#print foto.shape
#imprime la foto
# plt.imshow(foto)

z=np.array([1,2,3,4,5])

#imprime si hay numeros menres a 3 en la matriz, y su posicion [true true false false false]
print z<3
print z>3
#imprime los numeros mayores que 3 de la matriz
print z[z>3]

foto_masked=np.where(foto>100,255,0)
plt.imshow(foto_masked)