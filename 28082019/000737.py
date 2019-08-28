# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:56:37 2019

@author: piedi
"""


import numpy as np

a=np.linspace(1,12,6)  

#cambia la forma de imprimir, la imprime con 3 filas de dos elementos cada fila
#fila,columna
#guardamos la matriz a con el orden que queremos
b=a.reshape(3,2)

#una forma de hacerlo es directo, pero no se guarda 
print a.reshape(3,2)
#va a imprimir la matriz como la teniamos antes, con una sola fila, ya que se no se guarda
print '---------'
print a
print '---------'
print b
print 'cantidad de elementos de la matriz a'
print a.size
print 'cantidad de elementos de la matriz b'
print b.size