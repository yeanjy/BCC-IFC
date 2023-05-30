lista = []
while True:
    numeros = (input("Digite os numeros (tecle enter para sair): "))
    if numeros == "":
        break
    numeros = int(numeros)
    lista.append(numeros)
lista.sort()
for lista in lista:
    print(lista)