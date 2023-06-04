def precedencia(sinal):
    if sinal == "+" or sinal == "-":
        return 1
    elif sinal == "*" or sinal == "/":
        return 2
    elif sinal == "^":
        return 3
    else:
        return -1
    
sinal = ["+", "-", "*", "/", "^"]    
entrada = input("Digite o sinal: ")
resultado = precedencia(entrada)

if resultado == -1:
    print("Erro, nao eh um sinal matematico")
else:
    print(resultado)