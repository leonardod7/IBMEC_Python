# Exercicio 3 Listas
# Crie duas listas aleatoriamente com 10 números inteiros cada. Crie uma terceira lista de 20 elementos, cujos valores
# deverão ser compostos pelos elementos intercalados das duas outras listas

#######################################################################################################################

import random

lista1 = []
lista2 = []
lista3 = []

for i in range(10):
    numero = random.randint(0, 9)
    lista1.append(numero)
for i in range(10):
    numero = random.randint(0, 9)
    lista2.append(numero)
for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(f"{lista1}")
print(f"{lista2}")
print(f"{lista3}")