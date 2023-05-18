# Exercicio 3: IUsnado o random.randit e o index

import random

lista = [0]*10
for i in range(10):
    voto = random.randint(10, 19)
    voto = voto - 10
    lista[voto] = lista[voto]+1
    cid = i
print(lista)

for i in range(10):
    if lista[i] > cid/10:
        print(f" {i+10} = {lista[i]} ")
maximo = max(lista)
ganhador = lista.index(maximo)
print(f" o ganhador foi o candidato {ganhador+10} ")
