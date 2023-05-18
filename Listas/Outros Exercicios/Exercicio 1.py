# Exercício Sala de Aula 1 Listas

# Ler dois conjuntos de 5 numeros reais cada, armazenando-os em duas listas (x e y) e calcular o produto escalar,sendo
# que o produto escalar é dado por ; x0 * y0 + x1 * y1 .......................

x = [1 ,2 ,3 ,4 ,5]
y = [10 ,20 ,30 ,40 ,50]
soma = 0

for i in range(5):
    soma = soma + x[i ] *y[i]        # estamos acumulado as multiplicacoes
    print(soma)                      # o print dentro do for, mostra cada resultado iterado com o [i]

print(soma)                          # o print fora do for mostra a soma do valor total



