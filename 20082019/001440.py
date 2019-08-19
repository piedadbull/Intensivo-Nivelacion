# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:49:55 2019

@author: piedi
"""

millas1=3
millas2=10
millas3=11
millas4=12

#funcion para calcular millas en kilometros
def convertir(millas):
    km=1.6*millas
    return (km)
    
#llamamos a la funcion con las distintas millas que pusimos
solucion1=convertir(millas1)
solucion2=convertir(millas2)
solucion3=convertir(millas3)
solucion4=convertir(millas4)

#impresion de la cantidad de millas que pusimos arribas en kilometros
print (millas1),('millas son'),(solucion1),('kilometros')
print (millas2),('millas son'),(solucion2),('kilometros')
print (millas3),('millas son'),(solucion3),('kilometros')
print (millas4),('millas son'),(solucion4),('kilometros')