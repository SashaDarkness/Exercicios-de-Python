# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 22:53:20 2022

Chico tem 1,50 metro e cresce 2 centímetros por ano,
enquanto Zé tem 1,10 metro e cresce 3 centímetros por ano.
Construa um programa que calcule e imprima
quantos anos serão necessários para que Zé seja maior que Chico. 

@author: Sasha Caroline
"""

#ALTURA CONVERTIDA PARA CENTIMETRO
altura_chico = 150 
altura_ze = 110
ano_chico = 2
ano_ze = 3
anos = 0

while altura_chico >= altura_ze:   
   altura_chico += ano_chico
   altura_ze += ano_ze 
   anos += 1 
   
   #CONVERÇAO DA ALTURA CENTIMETRO PARA METROS
   alt_c = altura_chico / 100
   alt_z = altura_ze / 100
   
print(f'\n{anos} Anos necessários para Zé ser maior que Chico.')  
print('Altura que eles vão ter:\n'
      + f'- Chico: {alt_c} metro\n- Zé: {alt_z} metro') 
