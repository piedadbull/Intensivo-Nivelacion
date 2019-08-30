# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:17:44 2019

@author: piedi
"""

from matplotlib import pyplot as plt  

#rangos de edad, eje x
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

#salarios medios, eje y
dev_y = [38496, 42000, 46752, 49320, 53200,56000, 62316, 64928, 67317, 68748, 73752]
#salarios 2 (python), eje y
py_dev_y = [45372, 48876, 53850, 57287, 63016,65998, 70003, 70000, 71496, 75370, 83640]

#graficar linea,color y tipo de linea, marcador,y la simobologia
plt.plot(ages_x,dev_y, color='b',linestyle='--',marker='.', label='all devs')
plt.plot(ages_x,py_dev_y,color='b',marker='o', label='python')

#titulo del eje x, eje y y del grafico 
plt.xlabel('edades')
plt.ylabel('salario medio (USD)')
plt.title('salario medio (USD) por edad')

#simbologia de que linea es de que color
#plt.legend(['all devs','python' ])
plt.legend()

plt.show()







