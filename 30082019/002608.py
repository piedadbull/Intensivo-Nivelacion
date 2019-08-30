# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:44:42 2019

@author: piedi
"""

from matplotlib import pyplot as plt 
#se le puede dar un estilo al grafico que nos guste, como por ejemplo
plt.style.use('fivethirtyeight')

#rangos de edad, eje x
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

#salarios medios, eje y
dev_y = [38496, 42000, 46752, 49320, 53200,56000, 62316, 64928, 67317, 68748, 73752]
#salarios 2 (python), eje y
py_dev_y = [45372, 48876, 53850, 57287, 63016,65998, 70003, 70000, 71496, 75370, 83640]

js_dev_y = [37810, 43515, 46823, 49293, 53437,56373, 62375, 66674, 68745, 68746, 74583]

#graficar linea,color y tipo de linea, marcador, linewidth(grosor de la linea)y la simobologia
plt.plot(ages_x,dev_y, color='k',linestyle='--',marker='.', linewidth=3,label='all devs')
plt.plot(ages_x,py_dev_y,color='b',marker='o', label='python')
plt.plot(ages_x,js_dev_y,color='y',marker='*', label='javaScript')

#titulo del eje x, eje y y del grafico 
plt.xlabel('edades')
plt.ylabel('salario medio (USD)')
plt.title('salario medio (USD) por edad')

#simbologia de que linea es de que color
#plt.legend(['all devs','python' ])
plt.legend()

#cuadrilla en el grafico
plt.grid(True)

plt.tight_layout()

plt.show()