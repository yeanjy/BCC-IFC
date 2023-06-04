lista = []
while True:
    letra = input("Digite: ")
    lista.append(letra)
    if letra == "":
        break
del lista[-1]
lista = list(dict.fromkeys(lista))
print(lista)