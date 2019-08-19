# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 18:30:07 2019

@author: piedi
"""
#se crea un diccionario vacio para despues agregarle lo que queremos 
d={}
#key y valores para agregar al diccionario
d['George']=24
d['Tom']=32
d['Jenny']=16
d['10']=100

#ciclo for para leer el diccionario e ir imprimiendo cada key y valor asociado 
for key, value in d.items():
    print ('key:'),(key)
    print ('value:'),(value)
    print ('')