# Exercício 6 da Lista de Funções
# Faça uma que recebe a idade de um nadador por parâmetro e retorna, também a categoria desse nadador
# de acordo com a tabela abaixo
#   Idade              Categoria
# 5 a 7 anos           Infantil A
# 8 a 10 anos          Infantil B
# 11 a 13 anos         Juvenil A
# 14 a 17 anos         Juvenil B
# Maiores de 18        Adulto
# inclusive o 18

######################################################################################################################

def Id_Nadador (Idade):

    if Idade >= 5 and Idade <= 7:
        Categoria = "Infantil A"
    elif Idade >= 8 and Idade <= 10:
        Categoria = "Infantil B"
    elif Idade >= 11 and Idade <= 13:
        Categoria = "Juvenil A"
    elif Idade >= 14 and Idade <= 17:
        Categoria = "Juvenil B"
    else:
        Categoria = "Adulto"
    print(Categoria)

Idade_Nadador = int(input("Digite a Idade do Nadador (Maiores de 4 Anos): "))

if Idade_Nadador > 4:
    Resultado = Id_Nadador(Idade_Nadador)
    print(Idade_Nadador)
else:
    print("Digite a Idade no Intervalo Indicado")

