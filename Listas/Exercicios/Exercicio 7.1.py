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

vendedores_por_faixa = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# inicializar uma lista vazia do salário dos vendedores
salarios = []

# para cada vendedor:
for vendedor in range(4):
    #     lê vendas do vendedor
    total_vendas = float(input("Informe o total de vendas da semana: "))
    #     calcula e exibe salário
    salario = int(200 + 0.09 * total_vendas)
    print("Salário final: R$", salario)
    #     incluir o salário na lista de salários
    salarios.append(salario)
    #     adicionar 1 no elemento de lista
    vendedores_por_faixa[(salario - 200) // 100] += 1

# mostrar quantidade de vendedores por faixa
for faixa in range(9):
    limite_inf = 200 + 100 * faixa
    limite_sup = 299 + 100 * faixa
    print("Faixa", limite_inf, "-", limite_sup, "->", vendedores_por_faixa[faixa])