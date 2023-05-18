# Exercício 2 Listas
# Faça um Programa que leia 20 números inteiros e armazene-os numa lista. A seguir, crie 2 novas listas a partir
# dessa lista inicial, a primeira (par) contendo os números pares e a segunda (impar) contendo os números IMPARES.
# Imprima as três listas

#######################################################################################################################

lista = []
lista_pares = []
lista_impares = []

for i in range (5):     # criando lista. isso é padrao.
    num = int(input("Numero: "))
    lista.append(num)

for i in range (5):    # conferindo se a lista é par ou impar e criando um contador para adicionar na lista
    if lista[i] % 2 == 0:
        lista_pares.append(lista[i])   # adicionando os valores pares na lista
    else:
        lista_impares.append(lista[i]) # adicionando os valores ímpares na lista

print(lista)
print(lista_pares)
print(lista_impares)