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

def main():
    minha_cartela = cartela()
    print("+-----------------------------+")
    print("|  B  |  I  |  N  |  G  |  O  |")
    print("+-----------------------------+")
    for linha in range(5):
        for chave in minha_cartela:
            print("| {:3d}".format(minha_cartela[chave][linha]), end=" ")
        print("|")
    print("+-----------------------------+")


if __name__ == "__main__":
    main()
