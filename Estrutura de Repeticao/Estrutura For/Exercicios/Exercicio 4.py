# Trabalho 4 Estrutura de Repetição For

# Num sistema contábil de condomínio, lê-se do teclado inicialmente, o saldo do mês anterior. A seguir, ler os
# lançamentos diários, compostos de dia, valor e tipo (Débito ou Crédito). Calcular o saldo atualizado e imprimir
# em cada linha: O dia, o valor (se débito colocar um sinal de menos na frente do valor) e o saldo do dia.
# Considere que o mês tenha 30 dias

######################################################################################################################

Saldo_Anterior_C = 0
Saldo_Anterior_D = 0
Dias = 2

for i in range (Dias):
    Dia = int(input("Digite o Dia: "))
    Valor = float(input("Digite o Valor: "))
    Tipo = str(input("Digite o Tipo (C-Crédito ou D-Débito): "))
    if Tipo == "D":
        Saldo_Anterior_D = Saldo_Anterior_D - Valor
    else:
        Saldo_Anterior_C = Saldo_Anterior_C + Valor

    Saldo = Saldo_Anterior_C + Saldo_Anterior_D

    if Tipo == "D":
        print(f" Dia: {Dia}   Valor: - {Valor}  Saldo: {Saldo} ")
    else:
        print(f" Dia: {Dia}   Valor: + {Valor}  Saldo: {Saldo} ")

# Nao consigo gerar uma lista com um de baixo do outro
