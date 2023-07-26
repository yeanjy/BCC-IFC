import random

def senhaaleatoria():
    senha = ""
    contador = random.randint(7, 10)
    for _ in range(contador):
        ascii_value = random.randint(33, 126)
        character = chr(ascii_value)
        senha += character
    return senha

senha = senhaaleatoria()
print(senha)