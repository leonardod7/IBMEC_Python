# texo = o mar nao e para reclamar e sim para amar e aclamar se chamar

# quais são os índices de mar (onde comecam a palavra mar a partir de m) na frase acima, onde aparecem

# temos que usar fatiamento de lista

# precisamos comparar pedaços de 3 em 3 que é mar

texto = "o mar nao e para reclamar e sim para amar e aclamar se chamar "

for i in range(len(texto)):
    if texto[i:i+3] == "mar":
        print(i)