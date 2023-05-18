
# Exercicio 3 - Lista Funções
#Faça uma função que recebe por parâmetro um valor inteiro e positivo e retorna o valor lógico Verdadeiro caso
# o valor seja primo e Falso em caso contrário. Faça um programa que recebe um conjunto de 5 números e indique se
# o número é primo ou não

######################################################################################################################

def primo(num):
    if num == 1:
        msg = "nao é primo"
    elif num == 2:
        msg = "é primo"
    elif num % 2 == 0:
        msg = "não é primo"
    else:
        msg = "é primo"
        for k in range(2, num):  # o num é o número -1, se num for 10, teremos de 2 até 9
            if num % k == 0:
                msg = "não é primo"
        return msg


for i in range(5):
    numero = int(input("Digite um Numero: "))
    msg = primo(numero)
    print(numero, msg)