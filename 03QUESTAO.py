# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 23:29:46 2022

Crie um programa que lê 6 valores inteiros e, em seguida, 
mostre na tela os valores lidos na ordem inversa.

@author: Sasha Caroline
"""

vetor = [0]*6
inverso = list()

#INSERIR OS VALORES NO VETOR
print('--Entre com um valor na')
for i in range(len(vetor)):
   vetor[i] = int(input(f'Posição {i}: '))

#INVERTE A ORDEM DO VETOR  
posicao = len(vetor) - 1
while posicao >= 0:
    inverso.append(vetor[posicao])
    posicao = posicao - 1

print('-'*32) 
print('\nValores do vetor:',vetor)
print('\nValores INVERSO:',inverso)

