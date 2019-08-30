# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 21:33:05 2019

@author: piedi
"""

from numpy import np
from numpy import loadtxt

data=loadtxt('wind.data')
#separar llos datos 
#contiene todas las filas y las primeras tres columnas
dates=data[:,:3]
#todas las filas y las columnas desde la 3ra hasta la ultima
winds=data[:,3:]
#imprime el promedio mim max desviacion de la matriz
print (winds.mean(),winds.min(),winds.std())
#impirme el minimo de todas las columnas
print (winds.min(axis=0))
#imprime el min de las filas (dias)
print (winds.min(axis=1))
#ubicacion del max de cada fila
print (winds.argmax(axis=1))
#numero de fila del maximo 
row= winds.max(axis=1).argmax()
row,col=np.where(winds==winds.max())
print (dates[row])

#primer elemento de cada columa igual a 1 entonces iguala a enero
enero=dates[:,1]==1
print (winds[enero,:].mean(axis=0))

#para ver los datos de mi matriz, cantidad de filas y columnas 
print data.shape

