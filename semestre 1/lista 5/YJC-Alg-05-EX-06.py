
def censtring(frase, largura):
    novafrase = " "*largura +frase
    return novafrase

frase = input("Digite uma frase: ")
largura = int(input("Digite o deslocamento: "))
print(censtring(frase, largura))