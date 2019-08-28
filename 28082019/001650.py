# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:29:47 2019

@author: piedi
"""

import numpy as np

#para leer un archivonde texto o CSV 
datos=np.loadtxt('archivo.txt',dtype=np.uint8,delimiter=',',skiprows=1)

print datos