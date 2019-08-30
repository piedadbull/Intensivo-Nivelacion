# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:11:40 2019

@author: piedi
"""

import numpy as np

c=np.array([[0,1,2,3,4,5],[10,11,12,13,14,15],[20,21,22,13,14,15],[30,31,32,33,34,35],[40,41,42,43,44,5],[50,51,52,53,54,55]])
print c
#imprime la fila 0 desde el elemeto 3 al 4, o fila 0 colluma 3 y 4
print c[0,3:5]
#imprime desde el elemnto 4 hasta el final de filas y de columnas 
print c[4:,4:]
#imprime toda la columa 2
print c[:,2]
#imprime desde la fila 2 hasta la ultima fila, pero cada 1 filas, y lo mismo con las columnas, pero parte desde la columna 0 hasta la ultima
print c[2::2,::2]