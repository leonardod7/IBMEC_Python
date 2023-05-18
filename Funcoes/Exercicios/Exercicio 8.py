# Exercício 8 Lista de Funções
# Faça uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar. A função deve retornar um valor
# booleano.

######################################################################################################################

def Vlr_Int (x):
    resto = x % 2
    if resto == 0:
        return "Par"
    if resto != 0:
        return "Ímpar"


Valor = int(input("Digite o valor ínteiro: "))
Resultado = Vlr_Int(Valor)

if Resultado == "Par":
    print("Verdadeiro")
    print("Par")
else:
    print("Falso")
    print("Ímpar")