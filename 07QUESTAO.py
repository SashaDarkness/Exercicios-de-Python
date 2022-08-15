# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 22:57:17 2022

Construa um programa que calcule a média aritmética de vários valores
inteiros positivos, lidos externamente. O final da leitura acontecerá
quando for lido um valor negativo. 

@author: Sasha Caroline
"""

i = 1
valor = 1
media = 0
soma_valores = 0
total_valores = 0 

while valor != 0 :     
  print(f'\nInforme o {i}ª valor:')
  i += 1  
    
  valor = int(input('-> '))
  total_valores += 1 
    
  #FIM DO LOOP QUANDO O VALOR FOR NEGATIVO
  if (valor <= 0):
     print('\n---- Fim da operação.----\n')
     break
  else:   
     
     #SOMA DE TODOS INTEIROS POSITIVOS    
     soma_valores += valor
      
     #Média dos números inteiros
     media = soma_valores / total_valores 
       
print('- Soma dos valores inteiros:',soma_valores)
print('- Média dos valores inteiros:',media)
