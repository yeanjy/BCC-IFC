import string

def caracteresunico(a, b):
    a = a.translate(str.maketrans("", "", string.punctuation + " "))
    b = b.translate(str.maketrans("", "", string.punctuation + " "))

    return True if sorted(a)==sorted(b) else False


frase = input("Digite: ").upper()
frase2 = input("Digite: ").upper()
resultado = caracteresunico(frase, frase2)
print(resultado)