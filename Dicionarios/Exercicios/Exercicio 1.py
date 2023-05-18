# Exercicios lista - Tuplas e Dicionários
#
# # Exercicio 1

# Escreva um programa Python para criar uma lista de Tuplas a partir das listas abaixo:
# nomes_cores = ["Black", "Red", "Maroon", "Yellow", 'Green', 'Blue', 'Olive']
# codigos_hexa = ["#000000", "#FF0000", "#800000", "#FFFF00",  '#008000', '#0000FF', '#808000']
# A seguir crie um programa Python para pesquisar o nome de uma cor e exiba o código 	hexadecimal

nome_cores = ["Black", "Red", "Maroon", "Yellow", 'Green', 'Blue', 'Olive', ]
codigos_hexa = ["#000000", "#FF0000", "#800000", "#FFFF00",  '#008000', '#0000FF', '#808000', ]

cores = list(zip(nome_cores, codigos_hexa))
print(cores)

nome_cor = input("Digite o nome da cor: ")

# cores[i] significa que ele procura pelo índice que é rodado dentro do i, conforme tamanho da lista, até rodar o
# último número (7) que é o tamanho da lista. Ele vai de 0,1,2,3,4....7. Encontrando essa posição, no caso se colocarmos
# zero, ele encontrará nessa lista abaixo, a primeira tupla que tem posição zero dentro da lista:
# [('Black', '#000000'), ('Red', '#FF0000'), ('Maroon', '#800000'), ('Yellow', '#FFFF00'), ('Green', '#008000'), ('Blue', '#0000FF'), ('Olive', '#808000')]
# Ou seja, ele devolverá o : ('Black', '#000000'). Achando essa tupla, ao lado do [i] temos o [0] que é a posição
# onde está o nome da cor, pois ele pergunta no if se o nome da cor for igual, trazer código da cor.

for i in range(len(cores)):
    if cores[i][0] == nome_cor:
        print("Código: ", cores[i][1])      # 0 vai trazer a posicao da tupla que esta dentro da lista e o 1, é a
                                            # posição do código da cor

# caso quisessemos ao invés de fazer a busca informando o índice, podemos informar o elemento dentro do for, ao invés
# do [i] e ao invés de usar o range com o len para o tamanho da lista, usamos o próprio nome da lista, que no caso
# é "cores"
# vamos chamar entao o elemento de tupla (ele entende como elemento, a tupla dentro da lista, ou seja, quando falamos
# tupla, ou i, ou a, qualquer nome (porem no caso temos que colocar o nome da lista depois do "in", ele entende
# como o elemento dentro da lista, no caso, são as tuplas. Dentro dessa tupla, informamos apenas a posicao da cor
# para fazermos o if, ele compara com o nome da cor de input e gera o print do código através da posicap informada
# da tupla.

for tupla in cores:
    if tupla[0] == nome_cor:
        print("Código: ", tupla[1])
