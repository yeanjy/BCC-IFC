import random

def cartela():
    dicionario = {
        "B": None,
        "I": None,
        "N": None,
        "G": None,
        "O": None
    }

    for chave in dicionario:
        if chave == "B":
            dicionario[chave] = random.sample(range(1, 16), 5)
        elif chave == "I":
            dicionario[chave] = random.sample(range(16, 31), 5)
        elif chave == "N":
            dicionario[chave] = random.sample(range(31, 46), 5)
        elif chave == "G":
            dicionario[chave] = random.sample(range(46, 61), 5)
        elif chave == "O":
            dicionario[chave] = random.sample(range(61, 76), 5)

    return dicionario

def main(cartela):
    
    print("+-----------------------------+")
    print("|  B  |  I  |  N  |  G  |  O  |")
    print("+-----------------------------+")
    for linha in range(5):
        for chave in cartela:
            print("| {:3d}".format(cartela[chave][linha]), end=" ")
        print("|")
    print("+-----------------------------+")


def cartela_vencedora(cartela):
    for linha in cartela.values():
        if all(numero == 0 for numero in linha):
            return True

    for coluna in range(5):
        if all(cartela[chave][coluna] == 0 for chave in cartela):
            return True

    if (cartela['B'][0] == 0 and cartela['I'][1] == 0 and cartela['N'][2] == 0 and
        cartela['G'][3] == 0 and cartela['O'][4] == 0):
        return True

    if (cartela['B'][4] == 0 and cartela['I'][3] == 0 and cartela['N'][2] == 0 and
        cartela['G'][1] == 0 and cartela['O'][0] == 0):
        return True

    return False

def lista():
    lista = []