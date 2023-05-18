# Exercicio 4 Lista
# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos

#######################################################################################################################

Lista_Idade = []
Lista_Altura = []

for i in range(5):
    Idade = int(input("Idade: "))
    Altura = float(input("Altura: "))
    Lista_Idade.append(Idade)
    Lista_Altura.append(Altura)

media = sum(Lista_Altura) / len(Lista_Altura)
Cont = 0

for i in range(5):
    if Lista_Idade[i] > 13 and Lista_Altura[i] < media:
        Cont = Cont + 1

print(Cont)