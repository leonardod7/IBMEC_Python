# Trabalho 5 Estrutura de Repetição For

# Faça um programa que calcule a quantidade de combustível que pode ser colocada em uma aeronave e verifique se a
# aeronave pode levantar vôo ou não. Considere os seguintes critérios:

# O peso de decolagem da aeronave é sempre igual a 500.000 Kg;
# O avião possui 470 lugares.
# O peso de decolagem é composto pela soma do peso do combustível, do peso da carga, do peso dos passageiros;
# O peso do combustível é a quantidade do combustível (em litros) multiplicada pelo fator 1,5 Kg/l;
# A quantidade mínima de combustível para que a aeronave decole é de 100.000 l;
# O peso da carga é o somatório do peso dos “containers” de carga, em quilogramas (Kg);
# O peso dos passageiros é o somatório do peso de cada passageiro e de todos os volumes da sua bagagem;
# cada passageiro tem um peso estimado de 70 Kg para homens e 55 Kg para mulheres e cada volume de bagagem tem o (cont.)
# peso estimado de 15 Kg.

# O programa deve ler o número de “containers” e a seguir ler o peso de cada “container”. A seguir devem ser lidos
# os seguintes dados dos 470 passageiros: número do bilhete, sexo (M- Masculino ou F – Feminino) e quantidade de
# volumes. Devem ser a quantidade total de volumes de bagagem, o peso total dos passageiros, o peso da carga,
# a quantidade possível de combustível, e uma mensagem indicando a liberação da decolagem ou não

######################################################################################################################

Containers = 1
Peso_Carga_Total = 0
Qtde_Passageiros = 2
Soma_Peso_Passageiro_M = 0
Soma_Peso_Passageiro_F = 0
Soma_Volume = 0

Qtde_Combustivel = float(input("Digite a Quantidade de Combustível em Litros (min 100.000 litros): "))
Peso_Combustivel_Total = Qtde_Combustivel * 1.5

# Processamento 1 - Peso Containers

for i in range(Containers):
    Qtde_Containers = int(input("Digite a Quantidade de Containers com o Mesmo Peso: "))
    Peso_por_Container = float(input("Digite o Peso de Cada Container: "))
    Peso_Containers = Qtde_Containers * Peso_por_Container
    Peso_Carga_Total = Peso_Carga_Total + Peso_Containers

# Processamento 2 - Peso Passageiros e Volumes (Bagagens)

for i in range(Qtde_Passageiros):

    Numero_Bilhete = float(input("Digite o Número do Bilhete: "))
    Sexo_Passageiro = str(input("Digite o Sexo do Passageiro (M-Masculino F-Feminino): "))

    if Sexo_Passageiro == "M":
        Soma_Peso_Passageiro_M = Soma_Peso_Passageiro_M + 70
    else:
        Soma_Peso_Passageiro_F = Soma_Peso_Passageiro_F + 55

    Qtde_Volumes = int(input("Digite a Quantidade de Malas: "))
    Peso_Volume = Qtde_Volumes * 15
    Soma_Volume = Soma_Volume + Peso_Volume

Peso_Total_Passageiros = Soma_Peso_Passageiro_M + Soma_Peso_Passageiro_F + Soma_Volume

# Saída

Peso_Total_Decolagem = Peso_Combustivel_Total + Peso_Total_Passageiros + Peso_Carga_Total

print(f" O Peso total de decolagem é de: {Peso_Total_Decolagem} Kg O Limite para Voo é de 500.000 KG")

if Peso_Total_Decolagem > 500.0000:
    print(f" Liberação da Decolagem Autorizada ")
else:
    print(f" Liberação da Decolagem Não Autorizada ")