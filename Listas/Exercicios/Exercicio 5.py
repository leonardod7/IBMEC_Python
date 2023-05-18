# Exercicio 5 Listas
# Faça um programa que leia 50 valores do tipo float e armazene-os em uma lista. Após esta entrada de dados, faça:
# a.	Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# b.	Calcule e mostre a soma dos valores;
# c.	Calcule e mostre a média dos valores;
# d.	Calcule e mostre a quantidade de valores acima da média calculada;
# e.	Calcule e mostre a quantidade de valores abaixo de sete;

#######################################################################################################################

lista = []
soma = 0
cont = 0
cont7 = 0
for i in range(1, 6):
    num = float(input('digite o numero: '))
    lista.append(num)
    soma = soma + num
    media = soma / i

for i in range(1, 6):
    print(lista[i * -1])

for i in range(5):
    if lista[i] > media:
        cont = cont + 1
for i in range(5):
    if lista[i] < 7:
        cont7 = cont7 + 1

print(f"A media é {media}")
print(f"A soma é {soma}")
print(f"O quantidade de numeros maior que a media é {cont}")
print(f"O quantidade de numeros menor que 7 é {cont7}")
