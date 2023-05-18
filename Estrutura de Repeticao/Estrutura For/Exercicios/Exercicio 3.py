# Trabalho 3 Estrutura de Repetição For

# A Companhia de Seguros Pica Pau possui 100 corretores. Cada corretor recebe uma comissão segundo o valor de sua
# venda no mês, seguindo os critérios:

# e o valor da venda for maior que R$ 20.000,00 a comissão será de 20% do valor da venda;
# Se o valor da venda for entre R$ 10.000,00 e R$ 20.000,00 a comissão será de 15% do valor da venda;
# Se o valor da venda for menor que R$ 10.000,00 a comissão será de 10% do valor da venda.

# Faça um programa que leia o nome do corretor e o valor de sua venda e gere um relatório contendo:

# Nome de cada corretor com o valor de sua comissão
# Total de vendas da companhia no mês
# Total de comissão que a companhia pagou aos corretores.

######################################################################################################################

Soma_Comissao = 0
Qtde_Corretores = 2
Soma_Vendas = 0

# Processamento

for i in range(Qtde_Corretores):

    Nome_Corretor = str(input("Digite o Nome do Corretor: "))
    Vlr_Venda_Corretor = float(input("Digite o Valor da Venda: "))

    if Vlr_Venda_Corretor > 20000:
        Vlr_Comissao = Vlr_Venda_Corretor * 0.2
    elif Vlr_Venda_Corretor > 10000:
        Vlr_Comissao = Vlr_Venda_Corretor * 0.15
    else:
        Vlr_Comissao = Vlr_Venda_Corretor * 0.10
    Soma_Comissao = Soma_Comissao + Vlr_Comissao
    Soma_Vendas = Soma_Vendas + Vlr_Venda_Corretor
    print(Nome_Corretor)
    print(Vlr_Comissao)

# Saida

print(f"o vendedor {Nome_Corretor} vendeu {Vlr_Comissao}")
# nao estou conseguindo gerar um relatorio com os dois corretores

print(f" o valor total de vendas da companhia no mês é de: {Soma_Vendas} ")
print(f" o valor total pago de comissão pela companhia foi de: {Soma_Comissao} ")

