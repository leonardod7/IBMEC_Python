# Exercicio 5 - Lista Funções

#Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito quando ele é igual a soma dos
# seus divisores excetuando ele próprio. (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve
# retornar um valor booleano.

######################################################################################################################

def Num_Perfeito (x):

    Soma = 0

    for i in range (1, Valor):

        Resto = Valor % i

        if Resto == 0:
            Soma = Soma + i

    if Valor == Soma:
        return "Perfeito"
    else:
        return "Não é Perfeito"


Valor = int(input("Digite um valor maior que 1: "))
Resultado = Num_Perfeito(Valor)

if Resultado == "Não é Perfeito":
    print("Falso")
else:
    print("Verdadeiro")