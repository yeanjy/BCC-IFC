def precedencia(sinal):
    if sinal == "+" or sinal == "-":
        return 1
    elif sinal == "*" or sinal == "/":
        return 2
    elif sinal == "^":
        return 3
    else:
        return -1

def tokens(entrada):
    operacoes = "+-*/^"
    acumulador = ""
    tokens = []

    for i in entrada:
        if i == " ":
            continue

        if i in operacoes:
            if acumulador != "":
                tokens.append(acumulador)
                acumulador = ""
            tokens.append(i)
        else:
            acumulador += i

    if acumulador != "":
        tokens.append(acumulador)
    return tokens

entrada = input("Digite a expressão matemática: ")
infix = tokens(entrada)
operadores = []
posfix = []

for token in infix:
    if token.isdigit():
        posfix.append(token)
    elif token in "+-*/^":
        while operadores and operadores[-1] != "(" and precedencia(token) <= precedencia(operadores[-1]):
            posfix.append(operadores.pop())
        operadores.append(token)
    elif token == "(":
        operadores.append(token)
    elif token == ")":
        while operadores and operadores[-1] != "(":
            posfix.append(operadores.pop())
        if operadores and operadores[-1] == "(":
            operadores.pop()

while operadores:
    posfix.append(operadores.pop())

print("Expressão pós-fixa:", posfix)
