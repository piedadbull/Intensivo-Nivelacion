# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:31:31 2019

@author: piedi
"""
import numpy as np

#diferencia entre una lista y un array
#la losta hay que ir leyendo elemento por elemento
#el array no, se ejecuta en linezs mas cortas, por ende es mas rapido

lista=[1,2,3,4,5]
for i in range(len(lista)):
    lista[i]*=3

print lista
   
   
z=np.array([1,2,3,4,5])  
z*=3

print z