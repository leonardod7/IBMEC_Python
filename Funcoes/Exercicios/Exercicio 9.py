# Exercício 9 da Lista de Funções
# Fazer uma função que calcula e retorna o fatorial de um número inteiro qualquer.
# Fazer um programa que peça um número inteiro qualquer e exiba o fatorial do número lido

######################################################################################################################

def fat(y):

    Resultado = 1

    for i in range(1 ,Numero +1):
        Resultado *= i
    return Resultado

Numero = int(input("Digite o Fatorial: "))
Fatorial = fat(Numero)
print(Fatorial)