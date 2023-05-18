# Exercicio 7 Lista
# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor
# que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
# Escreva um programa (usando uma lista de contadores) que determine quantos vendedores receberam salários nos
# intervalos de valores abaixo. O programa deverá ler o total de vendas do vendedor e calcular e exibir o valor do
# salário. Ao final, mostre a quantidade de vendedores por faixa. A empresa possui 100 vendedores

# Cria uma fómula para chegar na posicao da lista a partir das comissoes sem fazer varios ifs aninhados

# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 - $1099

#######################################################################################################################

Lista_Vendedores = []
Lista_Cont = [0]*9

Qtde_vendedores = 5
Salario_Fixo = 200
Comissao = 0.09

# Adicionando as vendas em uma lista

for i in range(Qtde_vendedores):
    Vendas = float(input("Digite o total de vendas: "))
    Comissao_Venda = Comissao * Vendas
    Salario_Total = Salario_Fixo + Comissao_Venda
    Lista_Vendedores.append(Salario_Total)
print(Lista_Vendedores)

# Criando Contadores nas Listas

for Valor in Lista_Vendedores:
    if 200 <= Valor <= 299:
        Lista_Cont[0] += 1
    elif 300 <= Valor <= 399:
        Lista_Cont[1] += 1
    elif 400 <= Valor <= 499:
        Lista_Cont[2] += 1
    elif 500 <= Valor <= 599:
        Lista_Cont[3] += 1
    elif 600 <= Valor <= 699:
        Lista_Cont += 1
    elif 700 <= Valor <= 799:
        Lista_Cont += 1
    elif 800 <= Valor <= 899:
        Lista_Cont += 1
    elif 900 <= Valor <= 999:
        Lista_Cont += 1
    elif 1000 <= Valor <= 1099:
        Lista_Cont += 1


print(Lista_Cont)
print(Lista_Vendedores)
