# Exercício 7 Lista Funções
# Faça uma função que recebe um valor inteiro e verifica se o valor é positivo ou negativo.
# A função deve retornar um valor booleano

######################################################################################################################

def Vlr_Int (x):

    if x > 0:
        return "Positivo"
    else:
        return "Negativo"

Valor = int(input("Digite um Valor Inteiro: "))

Resultado = Vlr_Int(Valor)

if Resultado == "Positivo":
    print("Verdadeiro")
else:
    print("Falso")