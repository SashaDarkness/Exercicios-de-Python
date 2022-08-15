lista = [0]*10
cont = 0
par = list()

#entrada da lista
for i in range(len(lista)):
  lista[i] = int(input("Entre com um valor: "))
print('-'*30)

#Quantos valores pares
for i in range(len(lista)):
    if (lista[i] % 2 == 0):
        cont += 1
       
        par.append(lista[i])        
        
print(f'Total de números pares: {cont}')
print('Valores pares:',par)
