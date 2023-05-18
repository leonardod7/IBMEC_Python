# Exercicio Sala de Aula 2 Listas
# Calcule a media de 3 alunos usando lista

notas_aluno1 = []
notas_aluno2 = []
notas_aluno3 = []
qtde_alunos = 3

for i in range(qtde_alunos):
    cod = int(input("Digite o seu cod ( 1,2,ou3): "))
    if cod == 1:
        for j in range(qtde_alunos):
            nota1 = float(input("Digite a nota: "))
            notas_aluno1.append(nota1)
    elif cod == 2:
        for w in range(qtde_alunos):
            nota2 = float(input("Digite a nota: "))
            notas_aluno2.append(nota2)
    else:
        for k in range(qtde_alunos):
            nota3 = float(input("Digite a nota: "))
            notas_aluno3.append(nota3)

print(notas_aluno1)
print(notas_aluno2)
print(notas_aluno3)

media_aluno1 = sum(notas_aluno1) / len(notas_aluno1)
media_aluno2 = sum(notas_aluno2) / len(notas_aluno2)
media_aluno3 = sum(notas_aluno3) / len(notas_aluno3)

print(media_aluno1)
print(media_aluno2)
print(media_aluno3)