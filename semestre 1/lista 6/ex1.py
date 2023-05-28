lista = []
while True:
    numeros = int(input("Digite os numeros (tecle 0 para sair): "))
    lista.append(numeros)
    if numeros == 0:
        break
lista.sort()
del lista[0]
print(lista)