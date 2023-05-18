# Exercicio 6 Lista
# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor.
# Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores (1-6) e uma função para
# gerar números aleatórios, simulando os lançamentos dos dados.

#######################################################################################################################

Cont = [0]*7

for i in range (6):
    face = int(input("Digite a jogada: " ))
    Cont[face - 1] = Cont[face - 1] +1               # Colocamos o -1 para acessar a posição certa. Se o jogador
                                                     # digitar 1, precisamos acessar a posição 0, pois é onde está
                                                     # armazenado o primeiro valor

for i in range (6):                                  # queremos mostrar os contadores
    print(f"Índice: {i} Contador: {Cont[i]} ")