palavra = input("Digite uma palavra para verificar se e palindromo: ").lower()
palavrainvertida = palavra[::-1]
while palavra == palavrainvertida:
    print ("É um palindromo")
    break
else: 
    print ("Não é um palindromo")

