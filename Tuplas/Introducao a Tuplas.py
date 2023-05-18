# Introdução Tuplas

t = tuple()                               # tupla vazia
print(t)


t = tuple("teste")
print(t)

tupla1 = tuple("a",)
print(tupla1)       # uma tupla contendo apenas um elemento deve ser escrita com uma vírgula ao final

# 1) Quando usar tupla?
# Resposta: podem ser usadas como chaves de dicionários
# Funções com número variável de argumentos (*) acessam os argumentos por meio de tuplas


# zip é uma função que devolve uma lista de tuplas, onde cada tupla contem um elemento de cada sequência

s = "abc"
t = [0, 1, 2]
z = zip(s, t)

for i in z:
    print(i)                    # imprime apenas as tuplas

# pode-se usar a funcao list com zip. zip é um iterador e irá percorrer a sequência.

e = "abc"
f = [0, 1, 2]
g = list(zip(e, f))             # Usamos list para transformar a tupla em lista. é uma tupla dentro de uma lista
print(g)                        # imprime uma lista e dentro dela, uma tupla

Lista_Nome = list("Anne")
print(Lista_Nome)               # quando usamos lista, ele imprime letra a letra dentro da lista

Lista = list(zip("Anne", "1234"))  # quando usamos zip com lista, ele junta cada elemento da primeira lista com cada
print(Lista)                       # elemento da segunta.

# Se quisermos imprimir os dois elementos da tupla que estao na lista:
Lista = [('A', '1'), ('n', '2'), ('n', '3'), ('e', '4')]
for letra, num in Lista:        # Observe que quando colocamos no for, o primeiro nome e o segundo, ele entende
    print(num, letra)           # como os elementos dentro da tupla, no caso, posicao na tupla 0 e 1
    print(letra, num)