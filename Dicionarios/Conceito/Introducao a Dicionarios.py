# Introdução a Dicionarios

# Dicionários são:
# a - Estruturas que implementam mapeamentos
# b - um mapeamento é uma coleção de associações entre pares de valores. o primeiro elemento do par é chamado de
# "chave" e o segundo elemente de "conteúdo"

# a funcao dict é usada para construir dicionarios e requer como parametro:
# a - uma lista de tuplas, cada um com um par chave/conteudo, ou uma sequencia de itens no formato chave=valor
# nesse caso, as chaves precisam ser strings, mas sao escritas sem aspas

##
d = dict([(1,2),('Chave', 'conteudo')])
print(d)

notas = {'joao':9, 'maria': 10, 'roberto': 6}
notas.setdefault('pert', 8)     # esse metodo, valida se existe o nome pert e o valor 8 no dicionario. se nao existir
# ele adiciona, caso contrario, ele nao faz nada.
print(notas)

aluno = {"nome": "123 de oliveria", "matricula": 12345, "data de nascimento": "11/11/2000", "notas": {"ap1": 6.7, "ap2": 7.7, "ac": 4.5}}
print(aluno["nome"])
# ele printa:
# 123 de oliveria

print(aluno["notas"])
# ele printa:
# {'ap1': 6.7, 'ap2': 7.7, 'ac': 4.5}

print(aluno["notas"]["ap2"])
# ele printa:
# 7.7

for i in aluno:
    print(aluno[i])

# ele printa :
# 123 de oliveria
# 12345
# 11/11/2000
# {'ap1': 6.7, 'ap2': 7.7, 'ac': 4.5}