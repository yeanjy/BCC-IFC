import string
frase = input("Digite uma frase para verificar se e palindromo: ").lower()
frase = frase.strip()
frase = frase.translate(str.maketrans('', '', string.punctuation))
fraseinvertida = frase[::-1]
while frase == fraseinvertida:
    print ("É um palindromo")
    break
else: 
    print ("Não é um palindromo")
