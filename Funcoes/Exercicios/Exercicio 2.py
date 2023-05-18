# Exercicio 2 - Lista Funções
# Escreva uma função que recebe por parâmetro 3 notas de um aluno e uma letra. Se a letra for A o procedimento calcula a média aritmética
# das notas do aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2) e se for H, a sua média harmônica. A média calculada deve ser retornada.
# Faça um programa que peça as três notas de um aluno e chame a função criada acima para calcular os três tipos de média
# (Atenção: A função deve ser chamada para cada tipo de média).

######################################################################################################################

def imprime(tipo):
    if tipo.upper() == "A":
        return "Media Aritmética"
    elif tipo.upper() == "P":
        return "Média Ponderada"
    elif tipo.upper() == "H":
        return " Média Harmônica"
    else:
        return ""


def medias(n1, n2, n3, tipo):
    if tipo.upper() == "A":
        m = (n1 + n2 + n3)
    elif tipo.upper() == "P":
        m = (n1 * 5 + n2 * 3 + n3 * 2 ) /10
    elif tipo.upper() == "H":
        m = 3 / ( 1 /n1 + 1/ n2 + 1 / n3)
    else:
        m = 0
    return m


nota1 = float(input("Digite a Nota 1: "))
nota2 = float(input("Digite a Nota 2: "))
nota3 = float(input("Digite a Nota 3: "))

med = medias(nota1, nota2, nota3, "A")
print(imprime("A"), round(med, 2))

med = medias(nota1, nota2, nota3, "P")
print(imprime("P"), round(med, 2))

med = medias(nota1, nota2, nota3, "H")
print(imprime("H"), round(med, 2))