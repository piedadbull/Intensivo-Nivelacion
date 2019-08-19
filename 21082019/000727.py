# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:03:17 2019

@author: piedi
"""

b=['banana','apple','microsoft']
print (b)

#cambiamos el orden de la lista; ahora sera primero microsoft, apple y despues banana
#para esto creamos una variable auxiliar, que la usaremos para guardar lo que esta en la primera posiscion de la lista
x=b[0]
b[0]=b[2]
b[2]=x

print (b)


