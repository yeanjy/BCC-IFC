import random

lista = []
i = 0
while i < 10: 
    numeros = random.randint(0, 100)  
    lista.append(numeros)
    i = i + 1
lista.sort()
del lista[0]
del lista [-1]
print(lista)
