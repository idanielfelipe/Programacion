# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 23:08:41 2023

@author: pipe0
"""
numero = float(input("Ingrese un número: "))
precision = int(input("Ingrese la precisión deseada: "))
raiz = numero / 2
for _ in range(precision):
        raiz = (raiz + numero / raiz) / 2

print("La raíz cuadrada es:", raiz)