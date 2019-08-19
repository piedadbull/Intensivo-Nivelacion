# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 00:18:37 2019

@author: piedi
"""

#sumar solo los positivos.
#Diferencia de cuando es mejor usar un ciclo while o un for
#usamos el while porque podemos restringir solo sumar algunos elementos de la lista, si es que no supieramos el orden de los numeros que hay dentro de la lista

lista=[2,4,1,-5,-3,-6]
total=0
#variable para reccorer la lista
i=0

while lista[i]>0:
    total+=lista[i]
    #se le suma 1 a la variable para que vea el siguiente elemento de la lista
    i+=1
print (total)