# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 23:05:42 2022

Em uma eleição presidencial existem quatro candidatos. Os votos são informados através de códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:   

-	1,2,3,4 = voto para os respectivos candidatos; 
-	5 = voto nulo; 
-	6 = voto em branco;

Elabore um programa que leia o código do candidato em um voto.
Calcule e escreva:

-	Total de votos para cada candidato; 
-	Total de votos nulos; 
-	Total de votos em branco;

Como finalizador do conjunto de votos, tem-se o valor 0.

@author: Sasha Caroline
"""

voto_candidato = 1
c1 = 0 
c2 = 0 
c3 = 0 
c4 = 0 
c5 = 0 
c6 = 0

print('----- ELEIÇÃO ELEITORAL -----')
print('- VOCÊ PODERAR VOTAR NAS SEGUINTES OPÇÕES ABAIXO:'+
      '\n1- PARA VOTAR NO 1º CANDIDATO'+
      '\n2- PARA VOTAR NO 2º CANDIDATO'+
      '\n3- PARA VOTAR NO 3º CANDIDATO'+
      '\n4- PARA VOTAR NO 4º CANDIDATO'+ 
      '\n5- PARA VOTAR NULO' +
      '\n6- PARA VOTAR EM BRANCO')

while voto_candidato != 0:

   print('\nQual dos candidatos acima deseja votar?')
   voto_candidato = int(input('-> '))

   #FIM DO LOOP QUANDO O CODIGO FOR IGUAL A ZERO
   if (voto_candidato <= 0):
      print('\n------ Fim da operação.------')
      break   
   
   elif (voto_candidato == 1):
      c1 += 1 
   elif (voto_candidato == 2):
      c2 += 1   
   elif (voto_candidato == 3):
      c3 += 1    
   elif (voto_candidato == 4):
      c4 += 1     
   elif (voto_candidato == 5):
      c5 += 1     
   elif (voto_candidato == 6):
      c6 += 1     
   else:    
      print('\n---- OPÇÃO INVÁLIDA. ----\n')   
    
print(f'\n{c1} <- VOTARAM NO 1º CANDIDATO.')
print(f'\n{c2} <- VOTARAM NO 2º CANDIDATO.')
print(f'\n{c3} <- VOTARAM NO 3º CANDIDATO.')
print(f'\n{c4} <- VOTARAM NO 4º CANDIDATO.')
print(f'\n{c5} <- VOTARAM NULO.') 
print(f'\n{c6} <- VOTARAM EM BRANCO.')
