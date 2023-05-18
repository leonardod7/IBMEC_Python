# Exercicio 1 - Resolvendo com Tuplas

nomes = []
teles = []
ag_tupla = []

for i in range(2):
    nome = input('Nome:')
    tel = input('Telefone:')
    ag_tupla.append((nome, tel))

print(ag_tupla)

for i in range(1):
    nome = input('Nome:')
    for elem in ag_tupla:
        if elem[0] == nome:
            print('telefone:', elem[1])