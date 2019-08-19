# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 00:18:37 2019

@author: piedi
"""

#sumar solo los negativos con while.

lista=[7,5,4,4,3,1,-2,-3,-5,-7]
total=0
#variable para reccorer la lista
e=0
while e<len(lista):
    #si el elemento de la lista es negativo, se suma
    if lista[e] >0:
        total=total
    else:
        total+=lista[e]
    #pasamos al siguiente elemento de la lista
    e+=1
print total

