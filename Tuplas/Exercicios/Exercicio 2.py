# Exercicio 2: Utilizando a função ZIP para juntar listas

l1 = [1,2,3,4,5,6,7,8,9]
l2 = ['a','b','c','d','e','f','g','h','i']
l4 = [10,20,30,40,50,60,70,80,90]

l3 = list(zip(l1,l2,l4))

print(l3)

print(l3[7][2])
