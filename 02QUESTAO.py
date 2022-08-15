# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 23:33:36 2022

Escreva um programa que leia 10 números inteiros e os armazene
em um vetor. Imprima o vetor, o maior elemento e a posição
que ele se encontra.

@author: Sasha Caroline
"""

vetor = [0]*10
maior = 0
posicao = 0

print('--Entre com um valor na')
for i in range(len(vetor)):
   vetor[i] = int(input(f'Posição {i}: '))

   #MAIOR NÚMERO    
   if vetor[i] > maior:
      maior = vetor[i]   
      
   #POSICAO DO MAIOR NÚMERO DO VETOR
   if maior == vetor[i]:
       posicao = i 
         
print('-'*32) 
print('\nValores do vetor:',vetor)    
print(f'\nMaior valor: {maior} está na posição {posicao}.')

