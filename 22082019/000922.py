# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 16:09:25 2019

@author: piedi
"""
#se crea un total=0 como variable, la cual despues en el ciclo for va a ir sumando los numeros
total=0


for i in range(1,100):
    #multiplo de 3, al total se le suma el numero i
    if i%3==0:
        total+=i
    #multiplo de 5, al total se le suma el numero i.
    #si usamos if en vez de elif, los numero como el 15, que son multiplos de 3 y de 5 se suman dos veces.
    elif i%5==0:
        total+=i
    #otro caso no se suma
    else:
        total=total
        
print (total)
