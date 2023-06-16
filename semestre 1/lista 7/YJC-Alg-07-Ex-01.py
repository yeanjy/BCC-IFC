def caracteresunico(palavra):
    conjunto = set()
    for letra in palavra:
        if letra in conjunto:
            return False
        else:
            conjunto.add(letra)
    return True

palavra = input("Digite: ")
seila = caracteresunico(palavra)
print(seila)
