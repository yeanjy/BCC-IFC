import string
def sompalavras(frase):
    palavras = []
    frase = frase.translate(str.maketrans('', '', string.punctuation))
    palavras = frase.split()
    return palavras

frase = input("Digite uma frase: ")
frase = sompalavras(frase)
print(frase)