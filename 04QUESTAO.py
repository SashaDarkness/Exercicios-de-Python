# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 23:18:00 2022

Crie um programa que lê 6 valores inteiros pares e, em seguida,
mostre na tela os valores lidos na ordem inversa.

@author: Sasha Caroline
"""

valor = [0]*6  #vetor
cont = 0
par = list()

print('--Entre com um valor na')
for i in range(len(valor)):
   valor[i] = int(input(f'Posição {i}: '))

#Quantos valores pares
for i in range(len(valor)):
    if (valor[i] % 2 == 0):
        cont += 1
       
        par.append(valor[i])        

#INVERTE A ORDEM DO VETOR
inverso = list(reversed(par))    

print('-'*32) 
print('\nValores digitados:',valor)
print(f'\nTotal de números pares: {cont}')
print('\nValores PAR:',par)
print('\nValores PAR INVERTIDO:',inverso)


