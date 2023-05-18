# Exercicio 4: Número de Saltos

lista_nome_saltos = ["Primeiro Salto:","Segundo Salto:","Terceiro Salto:","Quarto Salto","Quinto Salto"]

lista_atletas= []
lista_medias = []

# a lista salto precisa ser criada dentro do for. a cada atleta nós recriamos a lista

for i in range(3):
    lista_atletas.append(input("Atleta;"))
    saltos = []
    for j in range (2):
        saltos.append(float(input(lista_nome_saltos[j])))
    media = sum(saltos) / len(saltos)
    lista_medias.append(media)
    print("Resultado Atleta: ")
    print(f" Atleta:{lista_atletas[i]} ")
    print(f" Saltos: {saltos}")
    print(f" media: {lista_medias[i]} ")
    
maior_media = max(lista_medias)
ind = lista_medias.index(maior_media)