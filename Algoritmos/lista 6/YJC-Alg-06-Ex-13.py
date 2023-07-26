def countRange(lista, valor_minimo, valor_maximo):
    count = 0
    for elemento in lista:
        if valor_minimo <= elemento < valor_maximo:
            count += 1
    return count

def main():
    lista = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    valor_minimo = 3
    valor_maximo = 8

    quantidade = countRange(lista, valor_minimo, valor_maximo)
    print(f"A quantidade de elementos na lista entre {valor_minimo} e {valor_maximo} é: {quantidade}")

main()
