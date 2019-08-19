# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 00:18:37 2019

@author: piedi
"""

#sumar solo los positivos.
#Diferencia de cuando es mejor usar un ciclo while o un for
#usamos el while porque podemos restringir solo sumar algunos elementos de la lista, si es que no supieramos el orden de los numeros que hay dentro de la lista

lista=[2,4,1,-5,1,-3,-6]
total=0
#variable para reccorer la lista

for e in lista:
    if e >0:
        total +=e
    else:
        total=total
print total