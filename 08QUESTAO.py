# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 22:49:57 2022

A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, 
coletando dados sobre o salário e número de filhos. A prefeitura 
deseja saber:   

a)	média do salário da população; 
b)	média do número de filhos; 
c)	maior salário; 
d)	percentual de pessoas com salário até R$100,00. 

O final da leitura de dados se dará com a entrada de um salário negativo.

@author: Sasha Caroline
"""

i = 1
salario = 1
total_soma_salario = 0
total_soma_filhos = 0
maior_salario = 0
total_pessoas = 0 
media_salarial = 0
media_filhos = 0 
cont = 0
porcentual_salarial = 0 

while salario != 0 :     
    print(f'{i}ª Pessoa:')
    i += 1
    
    salario = float(input('- Quanto ganha (salário)?: '))
    total_pessoas += 1  
    
    #Fim do loop quando o salário for negativo
    if (salario <= 0):
       print('\n---- Fim da operação.----')
       break
    else:    
       filhos = int(input('- Quantos filhos tem?: '))
       print('-'*30)      
       
    #SOMA DE TODOS OS SALÁRIOS E FILHOS INFORMADOS  
    total_soma_salario += salario
    total_soma_filhos += filhos 
    
    #MÉDIA TOTAL SALARIAL DA POPULAÇÃO
    media_salarial = total_soma_salario / total_pessoas
    
    #MÉDIA TOTAL DOS FILHOS DA POPULAÇÃO
    media_filhos = total_soma_filhos / total_pessoas

    #MAIOR SALÁRIO INFORMADO DA POPULAÇÃO
    if salario > maior_salario:
        maior_salario = salario
     
    #PORCENTUAL DO SALÁRIO MENOR OU IGUAL A R$100.00    
    if salario <= 100:
        cont += 1
        porcentual_salarial = (cont / total_pessoas) * 100
        
        
print('\n-Total do salário da população:',total_soma_salario) 
print('\n-Total de filhos da População:',total_soma_filhos)
print('\n-Maior salário informado: ',maior_salario) 
print('\n--- MÉDIA DA POPULAÇÃO: ---') 
print(f'- Por salário: R${media_salarial} \n- Por filho: {media_filhos}')
print(f'\n-> {cont} Pessoas ganham até R$100,00.')
print(f'- Com porcentual salarial de {porcentual_salarial} %')
