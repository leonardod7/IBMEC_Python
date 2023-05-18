# Exercício 1 Listas
# Faça um Programa que leia 10 notas, mostre as notas e a média, desvio padrão e variância na tela.
# OBS: variância somatório dos quadrados das diferenças das notas em relação a média dividido pela
# quantidade de médias. Desvio padrão é a raiz quadrada da variância

#######################################################################################################################

notas=[]
soma=0
variancia=0

for i in range (1,11):
    nota=int(input("Digite a sua nota"))
    soma=soma+nota
    notas.append(nota)
media=soma/10
for i in range(len(notas)):
    variancia=(nota-media)**2/10
desvio=variancia**1/2
print(notas)
print(f"{variancia} {desvio} {media}")