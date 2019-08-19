# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 12:28:40 2019

@author: piedi
"""
nombre1='YK '
altura_m1=2
peso_kg1=90

nombre2='hermana de YK '
altura_m2=1.8
peso_kg2=70

nombre3='hermano de YK '
altura_m3=2.5
peso_kg3=160

def calcular_bmi(nombre,altura_m,peso_kg):
    bmi=peso_kg/(altura_m**2)
    #print ('bmi:'), (bmi)
    if bmi<25:
        return 'bmi:'+str(bmi)+'; '+ nombre+'no esta sobrepeso'
        #return nombre+'no esta sobrepeso'
    else:
        return 'bmi: '+str(bmi)+'; '+ nombre+'esta sobrepeso'
        #return nombre+'esta sobrepeso'
        
        
#llamamos a la funcion con los parametros de las tres personas que tenemos    
resultado1=calcular_bmi(nombre1,altura_m1,peso_kg1)
resultado2=calcular_bmi(nombre2,altura_m2,peso_kg2)
resultado3=calcular_bmi(nombre3,altura_m3,peso_kg3)
#imprimimos el resultado de casa persona
print (resultado1)
print (resultado2)
print (resultado3)
