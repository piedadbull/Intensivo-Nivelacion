# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:40:47 2019

@author: piedi
"""

import numpy as np 
from skimage import io
import matplotlib.pyplot as plt

#lee una foto.png o jpg pero habria que cambiarle el nombre a foto.jpg
foto=io.imread('foto.png')

#type(foto)
#matriz de la foto
print foto.shape
#imprime la foto
plt.imshow(foto)

#se invierten las columnas de la matriz, por lo que la foto se da vuelta
plt.imshow(foto[:,::-1])

#se invierten las filas de la matriz, por lo que la foto queda como espejo
plt.imshow(foto[::-1])

#cortar la foto segun las filas y columnas que queremos
plt.imshow(foto[400:600,200:300])

#resuce la matriz a la mitad
plt.imshow(foto[::2,::2])
