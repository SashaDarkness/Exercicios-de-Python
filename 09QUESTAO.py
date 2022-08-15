# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 23:24:25 2022

10)	Faça um programa para ler a nota da prova de 15 alunos
e armazene num vetor, calcule e imprima a média geral.

@author: Darkness
"""

notas = [0]*15
cont = 1 
for i in range(len(notas)):
   notas[i] = int(input(f'Nota do {cont}º aluno: '))
   cont += 1
  
#Soma de todas as notas
soma = sum(notas)

#Média de todas as notas
media = sum(notas)/len(notas)

print('-'*32) 
print('\nValores das notas digitadas:',notas)
print('\nSoma de todas as notas:',soma)
print('\nMédia das notas dos 15 alunos',media)
