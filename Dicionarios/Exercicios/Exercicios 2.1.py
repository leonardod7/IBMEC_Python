# Exercicio 2.1 - é o mesmo que o exercicio 2 da pasta Exercícios no Diretório Dicionário, porém resolvido de forma diferente

def mediapon(notas,pesos):
    media = 0
    for j in range(3):
        media = media + (notas[j]*pesos[j]/10)
    return media

turmas ={'ana': [1.0, 2.0, 3.0],
         'beto': [4.0, 5.0, 6.0],
         'ze': [7.0, 8.0, 9.0],
         'ciça':[4.5, 6.0, 6.8],
         'duda':[7.0, 10.0, 9.8]
        }

pesos = (4,4,2)

for i in range(2):
    nome = input('Digite o nome: ')
    if nome not in turmas:
        print(f"Aluno {nome} não pertence a turma")
    else:
        notas = turmas[nome]
        media = mediapon(notas,pesos)
        print(f"Aluno:{nome}\nMédia:{media}")