# Exercicio 4 - Lista Funções

# Faça um procedimento que recebe por parâmetro os valores a, b, c de uma equação do segundo grau (ax2 + bx + c)
# e verifique se a função tem 1, 2 ou não tem raízes. Faça uma função para calcular o valor de delta da fórmula
# da fórmula de báskara. Faça uma função para calcular as raíz da função, recebendo com o parâmetro o valor b (negativo)
# e o valo de delta da função e retorna a raíz.

# Δ < 0, então a equação não possui resultados reais;
# Δ = 0, então a equação possui apenas um resultado real ou possui dois resultados iguais (essas duas afirmações são equivalentes);
# Δ > 0, então a equação possui dois resultados distintos reais.
# Faça um programa para receber os valores a,b e c de uma função de segundo grau e exiba as raízes caso existam.

######################################################################################################################

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b ** 2 - (4 * a * c)

if delta < 0:
    print("nao tem raizes")
elif delta == 0:
    raiz_1 = (- b + delta ** 1 / 2) / 2 * a
    print("raiz 1")
else:
    raiz_1 = (- b + delta ** 1 / 2) / 2 * a
    raiz_2 = (- b - delta ** 1 / 2) / 2 * a
    print(raiz_1)
    print(raiz_2)
