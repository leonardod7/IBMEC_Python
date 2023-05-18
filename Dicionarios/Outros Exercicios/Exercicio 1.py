# Exercício 1 - Resolvendo com Lista

nomes = []
teles = []
ag_tupla = []

for i in range(2):
    nome = input('Nome:')
    tel = input('Telefone:')
    nomes.append(nome)
    teles.append(tel)

print(nomes)
print(teles)

for i in range(1):
    nome = input('Nome:')
    for j in range(len(nomes)):
        if nomes[j] == nome:
            print('telefone:', teles[j])
