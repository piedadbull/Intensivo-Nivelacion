# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:02:27 2019

@author: piedi
"""

from matplotlib import pyplot as plt  

#rangos de edad, eje x
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
#salarios medios, eje y
dev_y = [38496, 42000, 46752, 49320, 53200,56000, 62316, 64928, 67317, 68748, 73752]

#graficar 
plt.plot(dev_x,dev_y)

#titulo del eje x, eje y y del grafico 
plt.xlabel('edades')
plt.ylabel('salario medio (USD)')
plt.title('salario medio (USD) por edad')

plt.show()














