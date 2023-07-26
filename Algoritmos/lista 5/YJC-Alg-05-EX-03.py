def frete(pecas):
    if pecas == 1 :
        custo = 10.95
    else :
        custo = 10.95 + 2.95*(pecas - 1)

    return custo

pecas = int(input("Digite a quantidade de pecas: "))
print (f"O total de pecas foi de {pecas}")
print("O custo do frete sera de R$", frete(pecas))