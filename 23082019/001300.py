# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 00:18:37 2019

@author: piedi
"""

#sumar solo los negativos con ciclo for

#se crea una lista con x elementos
lista=[7,5,4,4,1,-2,-3,-5,-7]
#variable que va sumando los numeros negativos
total=0
#recorrer los elementos e de la lista
for e in lista:
    #si es negativo se suma ese elemento al total
    if e<0:
        total+=e
    #si es positivo, el total queda igual, ya que no se suma nada.
    else:
        total=total
print (total)
