# Trabalho 2 Estrutura de Repetição For

# Uma pesquisa de rua sobre o Little Sister foi feita com 2875 pessoas. Cada entrevistado respondeu a um questionário,
# no qual constava:

# Sua idade;
# Sua opinião em relação ao (apenas um valor possível é válido):

# 1 - ótimo
# 2 - bom
# 3 - regular
# 4 - ruim
# 5 - péssimo

######################################################################################################################

Qtde_Entrevistados = 5
Soma_Opiniao1 = 0
Soma_Opiniao2 = 0
Soma_Opiniao3 = 0
Soma_Opiniao4 = 0
Soma_Opiniao5 = 0
Soma_Idade = 0

# Processamento

for i in range(Qtde_Entrevistados):

    Opiniao = int(input("Digite a sua Opinião (1-ótimo 2-bom 3-regular 4-ruim 5-péssimo): "))
    if Opiniao == 1:
        Soma_Opiniao1 = Soma_Opiniao1 + 1
    elif Opiniao == 2:
        Soma_Opiniao2 = Soma_Opiniao2 + 1
    elif Opiniao == 3:
        Soma_Opiniao3 = Soma_Opiniao3 + 1
    elif Opiniao == 4:
        Soma_Opiniao4 = Soma_Opiniao4 + 1
    else:
        Soma_Opiniao5 = Soma_Opiniao5 + 1

    Idade = int(input("Digite a Idade: "))
    if Idade > 65 and Opiniao == 5:
        Soma_Idade = Soma_Idade + 1

Total_Respostas = Soma_Opiniao1 + Soma_Opiniao2 + Soma_Opiniao3 + Soma_Opiniao4 + Soma_Opiniao5
Perc_SomaOpiniao2 = Soma_Opiniao2 / Total_Respostas

# Saída

print(f" a qtde de Pessoas que acham ótimo é: {Soma_Opiniao1} ")
print(f" o percentual de respostas bom é: {Perc_SomaOpiniao2} ")
print(f" a quantidade de pessoas acima de 65 anos que responderam péssimo é: {Soma_Idade} ")