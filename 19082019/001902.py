# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 11:31:30 2019

@author: piedi
"""
nombre='YK'
altura_m=2
peso_kg=90

#ecuacion para calcular sobrepeso. Si es mayor que 25 esta sobre peso, de lo contrario esta bien
bmi=peso_kg/(altura_m**2)
print ('bmi:'), (bmi)
if bmi<25:
    print (nombre),('no esta sobrepeso')
else:
    print (nombre),('esta sobrepeso')
    
