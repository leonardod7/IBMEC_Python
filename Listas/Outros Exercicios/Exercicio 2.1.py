# Exercicio Sala de Aula 2 Listas
# Calcule a media de 3 alunos usando lista por outra forma


MEDIA = []
alunos = 3

for i in range(alunos):
    nota1 = float(input("Digite a 1 nota:"))
    nota2 = float(input("Digite a 2 nota:"))
    media = (nota1+nota2)/2
    MEDIA.append(media)

mediaturma = sum(MEDIA) / len(MEDIA)
print(mediaturma)

print(MEDIA)

print( "MEDIA ALUNO             MEDIA TURMA")
print(f"{MEDIA[0]}             {mediaturma}")
print(f"{MEDIA[1]}             {mediaturma}")
print(f"{MEDIA[2]}             {mediaturma}")
