# Trabalho 1 Estrutura de Repetição For

# Numa sala de 46 alunos foi feita uma pesquisa onde se perguntou a idade e a altura de cada aluno. Deseja-se saber:
# A média de idade dos alunos.
# A média da altura dos alunos com mais de 20 anos

######################################################################################################################

Soma_Idade = 0
Soma_Altura = 0
Qtde_Alunos = 3

# Processamento

for i in range(Qtde_Alunos):
    Idade = int(input("Digite a Idade do Aluno: "))
    Altura = float(input("Digite a Altura do Aluno: "))
    Soma_Idade = Idade + Soma_Idade
    Soma_Altura = Altura + Soma_Altura

Media_Idade = Soma_Idade / Qtde_Alunos
Media_Altura = Soma_Altura / Qtde_Alunos

# Saida

print(Media_Idade)
print(Media_Altura)
