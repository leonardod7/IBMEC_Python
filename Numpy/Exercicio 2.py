# Faça um programa em Python que solicite ao usuário a ordem de uma matriz e depois os valores que compõem a matriz. Seu programa deve imprimir quantos múltiplos dos números 2 a 9 existem na matriz.


# O programa mostrado abaixo não possui validação de dados ou controle de erros/exceções, ou seja, espera-se que o usuário utilize corretamente o programa.
# Obs.: Os pontos que precedem as linhas não fazem parte do programa e devem ser ignorados, estão aí apenas para garantir a indentação do código.

num_linhas = int(input('Digite o numero de linhas: '))
num_colunas = int(input('Digite o numero de colunas: '))
linha = list()
matriz = list()
mult_dois = mult_nove = 0

for linha in range(num_linhas):
    for coluna in range(num_colunas):
        elemento = float(input(f'Digite o valor do elemento {linha+1}{coluna+1}: '))
        linha.append(elemento)
        if elemento % 2 == 0:
            mult_dois += 1
        if elemento % 9 == 0:
            mult_nove += 1
    matriz.append(linha.copy())
    linha.clear()
print(f'\nA matriz possui {mult_dois} múltiplos de 2 e {mult_nove} múltiplos de 9.')


# Comentários:

# --> O programa utiliza uma lista de listas para guardar os elementos da matriz, embora o programa não utilize os dados posteriormente.
# --> A leitura dos dados é feita através de dois laços for aninhados e foram considerados valores do tipo float.
# --> Logo após a leitura de cada dado, verificamos se o elemento é múltiplo de 2 e/ou 9 através do resto da divisão do elemento por esses números.
# --> No final do programa mostramos ao usuário a quantidade de múltiplos de 2 e de 9. Note que há múltiplos simultâneos de 2 e 9, esses são contabilizados 2 vezes.
# --> Na figura anexada é apresentado um exemplo de funcionamento e o código.