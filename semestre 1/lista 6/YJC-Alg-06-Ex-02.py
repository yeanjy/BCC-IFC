lista = []
while True:
    numeros = int(input("Digite os números (tecle 0 para sair): "))
    lista.append(numeros)
    if numeros == 0:
        break
lista = sorted(lista, key=int, reverse=True)
del lista[-1]
print(lista)
