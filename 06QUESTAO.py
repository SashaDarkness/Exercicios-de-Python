# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 23:08:47 2022

Escreva um programa que calcule a média aritmética das 3 notas
dos alunos de uma classe. O algoritmo deverá ler, além das notas,
o código do aluno e deverá ser encerrado quando o código for igual
a zero.

@author: Sasha Caroline
"""

notas = [0]*3
codigo_aluno = 1
soma = 0
media = 0
cont = 1

while codigo_aluno != 0:         
  codigo_aluno = int(input(f'Informe o código do {cont}º aluno: '))
  cont += 1
  
  #FIM DO LOOP QUANDO O CODIGO FOR IGUAL A ZERO
  if (codigo_aluno == 0):
     print('\n---- Fim da operação.----')
     break
  else: 
     
    #VETOR DAS 3 NOTAS DO ALUNO 
    for i in range(len(notas)):
       notas[i] = int(input('Informe a nota: '))
       
       #Soma das notas do vetor
       soma = sum(notas)
       
       #média das notas
       media = sum(notas)/len(notas)   

    print('-'*19)
    print(f'Notas: {notas}')
    print('- Código do aluno:',codigo_aluno) 
    print('- Soma das notas:',soma)   
    print(f'- Média das notas: {media}')
