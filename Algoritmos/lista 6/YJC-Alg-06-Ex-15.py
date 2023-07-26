def tokens(entrada):
    operacoes = "+-/*^"
    acumulador = ""
    tokens = []
    
    for i in entrada:
        if i == " ":
            continue
        
        if i in operacoes:
            if acumulador != "" :
                tokens.append(acumulador)
                acumulador = ""
            tokens.append(i)
        else:
            acumulador += i

    if acumulador != "":
        tokens.append(acumulador)
    return tokens



entrada = input("Digite: ")
saida = tokens(entrada)
print(saida)