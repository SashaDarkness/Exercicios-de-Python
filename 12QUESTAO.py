vetor = [0]*10
maior = 0
menor = 0

for i in range(len(vetor)):
   vetor[i] = int(input('Entre com um valor: '))

   if i == 0:
      maior = menor = vetor[i]
   else:
   #MAIOR NÚMERO    
     if vetor[i] > maior:
        maior = vetor[i]   
         
   #MENOR NÚMERO         
     if vetor[i] < menor:
        menor = vetor[i]      
         
print('-'*32) 
print('\nValores do vetor:',vetor)    
print(f'\nMaior valor: {maior}')
print(f'\nMenor valor: {menor}')
