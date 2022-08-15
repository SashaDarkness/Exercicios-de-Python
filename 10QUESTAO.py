#Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
lista = [0]*6

#entrando na lista.
for i in range(len(lista)):
  lista[i] = int(input("Entre com um valor: "))
print('-'*30,'\n')  
print('lista:',lista)

#soma das posições 0, 1 e 5.
soma = lista[0] + lista[1] + lista[5]
print(f'\nSoma dos valores {lista[0], lista[1], lista[5]}: {soma}')

#alterando o valor das posição 4.
lista[4] = 100
print(f'\nAlteração do valor da lista: {lista}')

#apresentando cada valor em uma linha.
print('\nPrint de cada valor da lista em uma linha:')
for i in range(len(lista)):
    print('\n',lista[i])
