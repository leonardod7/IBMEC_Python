# Exercicios lista - Tuplas e Dicionários
# Escreva um programa que lê três notas de vários alunos e armazena tais notas em um dicionário,
# onde a chave é o nome do aluno. A turma contém 10 alunos. Escreva uma função que retorna a média ponderada
# das notas do aluno, dados de entrada são:  as listas: notas e pesos. Os pesos são respectivamente
# 4, 4, 2 (armazenados em uma tupla).  Após a entrada de dados, desenvolva um trecho de código que solicite o
# nome do aluno, busque esse nome no dicionário de alunos e, achando-o, calcule a média, e exiba o nome,
# a média e informe também a sua situação:  aprovado ele precisa de 7 ou mais e reprovado significa
# média abaixo de 5, do contrário fará a prova PS.


# Exercicio 2

# para adicionarmos no dicionario, temos que colocar o nome do "dicionario"
# com o nome da chave que queremos informar, no caso [nome] será a chave
# na sequencia, colocamos o = para informar (o = seria o ":") qual o valor
# daquela chave informada

# Funcao Média Ponderada

def medpond(notas, pesos):
    media = 0
    for k in range(3):
        media = media + ((notas[k]*pesos[k])/10)
    return media

# Leitura das notas e do nome e armazenagem no dicionario


turmas = {}

for i in range(3):
    nome = input("Digite o seu nome: ")
    notas = []
    for j in range(3):
        nota = float(input("Digite a nota: "))
        notas.append(nota)
    turmas[nome] = notas
print(turmas)


# Saída para solicitar o nome do aluno e imprimir os dados de média e validar se ele vai para a PS ou não


pesos = (4, 4, 2)

for i in range(3):
    name = input("Digite o nome do aluno: ")
    if name not in turmas:
        print(f" O Aluno {name} não percente a turma ")
    else:
        nf = turmas[name]
        media_aluno = medpond(nf, pesos)
        print(f"Aluno: {name} \nMédia: {media_aluno}")
        if media_aluno >= 7.0:
            print(f"Aluno Aprovado")
        elif media_aluno >= 6.0:
            print(f"Aluno fará a prova PS")
        else:
            print(f"Aluno Reprovado")
